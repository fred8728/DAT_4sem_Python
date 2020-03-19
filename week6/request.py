import api_keys
import requests 
import json

def main_data():
    url = "http://api.openweathermap.org/data/2.5/forecast"
    req = requests.get(url, params={'q': 'Copenhagen,dk', 'mode': 'json', 
                                'units': 'metric', 
                                'appid': api_keys.GITHUB_API_KEY})
    req_json = json.loads(req.weather.value)

    print(req_json)

main_data()