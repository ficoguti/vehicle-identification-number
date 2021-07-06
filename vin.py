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

def main():
    vin = input("Enter a Vehicle Identification Number: ")
    headers = get_auth()
    DECODE_URL = 'http://api.carmd.com/v3.0/decode?vin='
    r = requests.get(DECODE_URL + vin, headers=headers)
    
    #print(r.statuscode)
    print(r.json())
    
if __name__ == "__main__":
    main()