import requests
import pandas as pd
import cv2
import os
import sqlalchemy
from sqlalchemy import create_engine
import plotly.express as px


def get_auth():
    AUTH_KEY = 'ODYwYmMxNjQtNjE3OS00OGM5LWEwZGYtN2FkZTQ4ZjY0NmE3'
    TOKEN = 'cddae0cb72134c408a0836016130be55'

    headers = {
      "content-type": "application/json",
      "authorization": 'Basic {key}'.format(key=AUTH_KEY),
      "partner-token": TOKEN
    }

    return headers


def parse_data(vin):
    headers = get_auth()
    DECODE_URL = 'http://api.carmd.com/v3.0/decode?vin='
    IMAGE_URL = 'http://api.carmd.com/v3.0/image?vin='
    decoder = requests.get(DECODE_URL + vin, headers=headers).json()

    message = decoder['message']
    data = decoder['data']
    if data is not None and message['code'] == 0:
        print('Year/Make/Model:', data['year'], data['make'], data['model'])
        print('Manufacturer:', data['manufacturer'])
        print('Engine:', data['engine'])
        if data['trim']:
            print('Trim:', data['trim'])
        print('Transmission:', data['transmission'])
        
        # looks for image of vehicle
        img = requests.get(IMAGE_URL + vin, headers=headers).json()
        img = img['data']
        if img['image']:
            print('Image:', img['image'])
            
        return decoder
    else:
        print('Invalid code')
        return None


def loadSQLfromFile(filename, database_name):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' +
              database_name + ';"')
    os.system("mysql -u root -pcodio " + database_name + " < " + filename)


def saveSQLtoFile(filename, database_name):
    os.system("mysqldump -u root -pcodio " + database_name + " > " + filename)


def createEngine(database_name):
    engine = create_engine("mysql://root:codio@localhost/" + database_name)
    return engine


def createDataFrame(r, vin):
    data = r['data']
    d = {
        'VIN': [vin],
        'year': [data['year']],
        'make': [data['make']],
        'model': [data['model']]
    }

    df = pd.DataFrame(data=d)
    return df


def saveDatasetToFile(database_name, table_name, filename, dataframe):
    currentData = loadDataset(database_name, table_name, filename)
    if dataframe['VIN'].values not in currentData['VIN'].values:
        dataframe.to_sql(table_name, con=createEngine(database_name),
                         if_exists='append', index=False)
        saveSQLtoFile(filename, database_name)
        print('VIN added to database')
    else:
        print('VIN already in database')


def clearDatasetInFile(database_name, table_name, filename):
    os.system('mysql -u root -pcodio -e "TRUNCATE TABLE ' + database_name +
              "." + table_name + ';"')
    saveSQLtoFile(filename, database_name)


def loadDataset(database_name, table_name, filename):
    loadSQLfromFile(filename, database_name)
    df = pd.read_sql_table(table_name, con=createEngine(database_name))
    return df


def plotCarsByYear(dataset):
    cars_made_data = dataset['YEAR'].value_counts().rename_axis(
            'year').reset_index(name='cars')
    fig = px.scatter(cars_made_data, x='year', y='cars',
                     labels={
                         "year": "Year",
                         "cars": "Cars Produced"
                     },
                     title="Number of Cars Produced Per Year")

    fig.update_layout(
        yaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1
        )
    )

    fig.write_html('carsproducedyear.html')


def main():
    vin = ''
    while(len(vin) != 17):
        vin = input("Enter a Vehicle Identification Number: ")
        if(len(vin) != 17):
            print('Please enter a valid VIN')

    # print vehicle info to user
    decoder = parse_data(vin)
    database_name = 'vindecoder'
    filename = 'vin-queries.sql'
    table_name = 'queries'

    # Use this to clear the current database
    # loadSQLfromFile(filename, database_name)
    # clearDatasetInFile(database_name, table_name, filename)

    if(decoder is not None):
        dataframe = createDataFrame(decoder, vin)  # organize data

        loadSQLfromFile(filename, database_name)
        # save user query to database
        saveDatasetToFile(database_name, table_name, filename, dataframe)
        dataset = loadDataset(database_name, table_name, filename)
        print(dataset)

        # add dataset to interactive visual
        plotCarsByYear(dataset)
    else:
        # either not a valid VIN or no more query credits :(
        print('VIN not found.')


if __name__ == "__main__":
    main()
