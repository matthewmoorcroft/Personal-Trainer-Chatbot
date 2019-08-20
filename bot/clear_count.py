import requests

url = "https://api.telegram.org/bot725490953:AAF79oRlrKI6SqZNCqjOLRtRwzmOF7A-Yt4/getUpdates?offset=224712604&limit=100"

res = requests.get(url)
print(res.json())
