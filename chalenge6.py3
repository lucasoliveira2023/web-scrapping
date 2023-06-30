import requests
import os
from bs4 import BeautifullSoup
from babel.numbers import format_currency

countries = []

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"
headers = {'User_Agent':'user_agent'}

def find_countries():
  url = "https://www.iban.com/currency-codes"


request = request.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
        itens = row.find_all("td")
        name = itens[0].text
        code = itens[2].text
        if code != "":
                country ={
                'name':name,
                'code':code
    }
countries.append(country)

def menu():
  find_countries()
  for index,country in enumerate(countries):
    print(f"{index} , {country['name']}")

  print("bem-vindos ao negociador de moedas")
  print("escolha o numeros dos países que deseja negociar")
  try:
    choice = int(input())
    if choice > len(countries):
      print("não tem escolha um numero da lista")
    else:
      country = countries[choice]
      print(f"(x) {country['name']} \Moeda: {country['code']}")
      choice_1 = country['code']
      print("para qual país converter")
      try:
        choice = int(input())
        country = countries[choice]
        print(f"(x) {country['name']} \nMoeda:{country['code']}")
        choice_2 =country['code']
        return convert(choice_1, choice_2)
      except:
        print("voce tem que digitar um numero!")

  except:
    print("voce tem que digitar um  numero!")


def convert(choice_1, choice_2):
  valor = int(input(f"digite o valor a ser convertido"))
  url = f"https://wise.com/gb/currency-converter/{choice_1}-to-{choice_2}-rate?amount={valor}"
  r_url = requests.get(url, headers={'User_Agent':'user_agent'})
  soup = BeautifullSoup(r_url.text, "html_parser")
  rate = float(soup.find('span', class_='text-sucesso').string)
  rate_math = valor * rate
  print(format_currency(rate_math, choice_2))
  restart()

def restart():
  option = input("Deseja conveter mais alguma moeda? S/N").lower()

  if option == 'S':
    os.system('clear')
    menu()

  elif option == 'n':
    print("programa finalizado")
  else:
    print("opção invalida")
    restart()

menu()