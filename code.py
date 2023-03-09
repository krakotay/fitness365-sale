import requests
from base64 import b64encode
import json

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

#Необходимо ввести данные, я их из соображений безопасности уберу
username = ""
password = ""

headers = { 'Authorization' : basic_auth(username, password) }



#Сам код

phone = '74950000000'
amount = '1'
description = 'Безлимит на 12 месяцев'
productId = "Безлимит 12 месяцев"
payType = "Beznal"
cashdeskId = ""
activationDate = "01.01.2023"
data2 = {'phone': phone, 'amount': amount, 
'description': description, 'productId' : productId, 'payType': payType, 'cashdeskId': cashdeskId}

get_sale = requests.post('https://w.fitness365.ru/api/v1/saleByClientPhone', json=data2, headers=headers)

print(get_sale.text)
