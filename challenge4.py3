import requests


def menu():
  escolha = str(input("verificar mais um site S/N")).lower()
  if escolha == "s":
    main() 
  elif escolha == "n":
    print("encerra!")
    return
  else:
    print("opcao invalida")
    menu()

    
def main():
  print("insira um site para verificar:(separado por virgula)")
  urls = str(input()).lower().split(",")

  for url in urls:
    url = url.strip()
    if "." not in url:
     print(url,"cara url invalida")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        requisicao = requests.get(url)
        if requisicao.status_code == 200:
          print(url,"url online")
        else:
          print,(url,"site offline")
        print(requisicao.status_code)
      except:
          print(url,"erro")

  menu()

main()