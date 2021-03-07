import requests

data = requests.get("https://www.kivano.kg/product/view/sotovyy-telefon-xiaomi-mi-10t-6-128gb-kosmicheskiy-chernyy")
print(data.content)
print(data.text)
print(data.json())