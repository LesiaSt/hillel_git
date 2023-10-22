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

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      " Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46"
}
request_bin = requests.get("http://httpbin.org/headers",headers = headers, verify = False)
print(request_bin.text)