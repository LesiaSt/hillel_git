import requests
from API_KEY import API_TOKEN

param = {
        "q": "Kyiv",
        "appid":API_TOKEN,
        "units": "metric"
}
new_request = requests.get('https://api.openweathermap.org/data/2.5/weather',
                           params=param, verify=False)
x = new_request.json()
print(x['main']['temp'])
print(new_request.headers)