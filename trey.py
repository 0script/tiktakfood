import requests

API_KEY1='db7bfcd23fb848ba9b98b2376182ad75'
API_URL='https://ipgeolocation.bstractapi.com/v1/?api_key='+API_KEY1

def geo_ip_location(ip):
    #return eval(requests.get(API_URL+'&ip_address='+ip).encoding('utf-8'))
    try:
        r = requests.get(API_URL, params={'ip_address': ip})
        return r.json()
    except requests.exceptions.RequestException as e:
        raise e

try:

    geo_ip_location('127.0.0.1')
except Exception as e:
    print('Error cannot proceed')
