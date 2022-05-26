import requests
URL = 'https://www.amazon.in/Renewed-Vivo-Sunshine-128GB-Storage/dp/B09V1QMFTL/ref=sr_1_5?keywords=vivo+v23&qid=1652682250&s=electronics&sr=1-5'

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
}

page = requests.get(URL,headers = headers)

print(page)
