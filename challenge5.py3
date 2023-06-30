import os
import requests
from bs4 import BeautifulSoup
os.system("clear")

url = "https://www.iban.com/currency-codes"
countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  itens = row.find_all("td")
  name = itens[0].text
  code = itens[2].text
  if name in code:
    if name != "no universal currency":
      country = {
        'nome': name.capitalize(),
        'code': code
      }
      countries.append(country)

def menu():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("escolha um pais que esta na lista:")
      menu()
    else:
      country = countries[choice]
      print(f"vc escolheu{country['name']}\no codigo da moeda é {country['code']}")
  except ValueError:
    print("isso não é um numero!!!")
    menu()

print("seja bem-vindo ao negociador de moedas")
print("escolha pelo numero da lista o pais que deseja consultar o codigo da moeda")

for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

menu()