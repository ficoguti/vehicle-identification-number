import requests

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
    else:
        print('Invalid code')

def main():
    vin = ''
    while(len(vin) != 17):
        vin = input("Enter a Vehicle Identification Number: ")
        if(len(vin) != 17):
            print('Please enter a valid VIN')
    
    headers = get_auth()
    DECODE_URL = 'http://api.carmd.com/v3.0/decode?vin='
    r = requests.get(DECODE_URL + vin, headers=headers).json()
    print(r)
    parse_data(r)
   

if __name__ == "__main__":
    main()