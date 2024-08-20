import requests 

url = 'https://cricbuzz-cricket.p.rapidapi.com/mcenter/v1/41881/comm'
headers = {
    'x-rapidapi-key': 'd3668d28ddmsh899b147fa69e9cdp123fb6jsn03895650f2ed',
    'x-rapidapi-host': 'cricbuzz-cricket.p.rapidapi.com'
}
response = requests.get(url, headers=headers)
print(response.json())