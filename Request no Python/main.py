import json
import requests

informacoes = {"Nome": "João", "Sobrenome": "Master"}

''' 
requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
print(requisicao)
print(requisicao.json())

'''

requisicao_firebase = requests.get("https://teste-lib-requests-48621-default-rtdb.firebaseio.com/.json")
print(requisicao_firebase)
print(requisicao_firebase.json())

informacoes = {"Nome": "João", "Sobrenome": "Master"}
requisicao_firebase = requests.post("https://teste-lib-requests-48621-default-rtdb.firebaseio.com/.json", json=informacoes)
print(requisicao_firebase)
print(requisicao_firebase.json())

informacoes = {"Nome": "Carlos", "Sobrenome": "Mendes"}
requisicao_firebase = requests.post("https://teste-lib-requests-48621-default-rtdb.firebaseio.com/.json", json=informacoes)
print(requisicao_firebase)
print(requisicao_firebase.json())


informacoes = {"Nome": "Mario", "Sobrenome": "Bross"}
requisicao_firebase = requests.patch("https://teste-lib-requests-48621-default-rtdb.firebaseio.com/-NpPsucodniHRgm-rytD.json", json=informacoes)
print(requisicao_firebase)
print(requisicao_firebase.json())

requisicao_firebase = requests.delete("https://teste-lib-requests-48621-default-rtdb.firebaseio.com/-NpPsucodniHRgm-rytD.json", json=informacoes)
print(requisicao_firebase)
print(requisicao_firebase.json())