import requests
import pandas as pd
import os
import sqlalchemy
from sqlalchemy import create_engine

def get_auth():
    AUTH_KEY = 'ODYwYmMxNjQtNjE3OS00OGM5LWEwZGYtN2FkZTQ4ZjY0NmE3'
    TOKEN = 'cddae0cb72134c408a0836016130be55'

    headers = {
      "content-type":"application/json",
      "authorization":'Basic {key}'.format(key=AUTH_KEY),
      "partner-token":TOKEN
    }

    return headers


def parse_data(r):
    message = r['message']
    data = r['data']
    if (message['code'] == 0):
        print(data['year'], data['make'], data['model'], data['manufacturer'],
              data['engine'], data['trim'], data['transmission'])
        return True
    else:
        print('Invalid code')
        return False

        
def loadSQLfromFile(filename, database_name):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' + database_name + ';"')
    os.system("mysql -u root -pcodio " + database_name + " < " + filename)
    
    
def saveSQLtoFile(filename, database_name):
    os.system("mysqldump -u root -pcodio " + database_name + " > " + filename)
    
    
def createEngine(database_name):
    engine = create_engine("mysql://root:codio@localhost/" + database_name)
    return engine


def createDataFrame(r, vin):
    data = r['data']
    d = {
        'VIN' : [vin],
        'year' : [data['year']],
        'make' : [data['make']],
        'model' : [data['model']]
    }
    
    df = pd.DataFrame(data=d)
    return df


def saveDatasetToFile(database_name, table_name, filename, dataframe):
    dataframe.to_sql(table_name, con=createEngine(database_name), if_exists='append', index=False)
    saveSQLtoFile(filename, database_name)


def loadDataset(database_name, table_name, filename, update=False):
    loadSQLfromFile(filename, database_name)
    df = pd.read_sql_table(table_name, con=createEngine(database_name))
    if update:
        return createDataFrame(None, None)
    else:
        return df


def main():
    vin = ''
    while(len(vin) != 17):
        vin = input("Enter a Vehicle Identification Number: ")
        if(len(vin) != 17):
            print('Please enter a valid VIN')
    
    headers = get_auth()
    DECODE_URL = 'http://api.carmd.com/v3.0/decode?vin='
    r = requests.get(DECODE_URL + vin, headers=headers).json()
    valid = parse_data(r)
    
    if(valid):
        database_name = 'vindecoder'
        filename = 'vin-queries.sql'
        table_name = 'queries'
        dataframe = createDataFrame(r, vin)

        loadSQLfromFile(filename, database_name)
        dataset = loadDataset(database_name, table_name, filename)
        saveDatasetToFile(database_name, table_name, filename, dataframe)


if __name__ == "__main__":
    main()