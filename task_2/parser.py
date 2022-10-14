import requests
from bs4 import BeautifulSoup
import json

def fetch(url, params):
    headers = params['headers']
    body = params['body']
    if params['method'] == 'GET':
        return requests.get(url, headers=headers)
    if params['method'] == 'POST':
        return requests.post(url, headers=headers, data=body)



card = fetch("https://basket-05.wb.ru/vol735/part73512/73512949/info/ru/card.json", {
    "headers": {},
    "referrerPolicy": "no-referrer-when-downgrade",
    "body": None,
    "method": "GET"
});

print(card.status_code)
print(card.json().keys())

article = card.json()['nm_id']
print(article)

brand = card.json()['selling']['brand_name']
print(brand)

article_name = card.json()['imt_name']
print(article_name)