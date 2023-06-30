from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

#setup para usar webdriver no repl.it
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

#driver
driver = webdriver.Chrome(options=chrome_options)
#aqui estou deixando o tamanho do navegador (tamanho da janela)padronizado :)
# pois se a janela for muito pequena o instagram abre a versão 'mobile' ou com layout diferente. Então apenas digo abaixo "Quero que o navegador seja 1024 x 768"
driver.set_window_size(1024, 768)

print(f"insira a url da postagem")
url_post =input('')
print("espere")

url_ig = "https://instagram.com/"
driver.get(url_ig)
sleep(6)



##botões,inputs
input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
input_username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/buttom/div')

#faz ações
input_username.send_keys("####")
input_password.send_keys("####")
slepp(1)
btn_login.click()
sleep(3)

#apos o login abre o poster
driver.get(url_post)
sleep(5)

#agora tentativa e excessão
try:
  btn_more_coments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')

  while btn_more_coments.is_displayed():
    btn_more_coments.click()
    sleep(4)
    btn_more_coments = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button')

except Exception as err_msg:
  print(err_msg)
  pass
sleep(3)



comments = driver.find_elements_by_class_name("gElp9")
list_users =[]


for comment in comments:
  username = comment.find_elements_by_class_name("_6lAjh").text
  if username not in list_users:
    list_users.append(username)


winner = random.choice(list_users)

print(f"{len(list_users)} usuarios participando do sorteio")
print(f" selecionado: {winner}")
