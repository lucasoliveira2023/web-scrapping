def is_on_list(a_code, a_list=[]):
    return a_code in a_list

def add_tracking_code(a_code, a_list=[]):
    a_list.append(a_code)

def add_remove_code(a_code, a_list):
    a_list.remove(a_code)

def get_tracking_code(a_code, a_list):
    return a_list[a_code]

def sum_two_lists(list_one, list_two):
  return len(list_one) + len(list_two)

def join_two_lists(list_one, list_two):
  return list_one + list_two

def get_the_biggest(a_list):
  return max(a_list)

def count_in_list(a_value, a_list):
  return a_list.count(a_value)

def sum_total(a_list):
  return sum(a_list)

def remove_tracking_code(a_code, a_list =[]):
    a_list.remove(a_code)

## use este espaço de cima do código para
## declarar funções e escrever seu código

#####################################################
#####!! NÃO EDITE O CÓDIGO ABAIXO DESTA LINHA !!#####

tracking_codes = ["JN426598162BR", "JN426598255BR","JN426598247BR","JN426598145BR","JN426598057BR","JN426598074BR","JN426598233BR","JN426598220BR","JN426598278BR","JN426598281BR","JN426598043BR","JN426598030B"]

# Verificar se um código está na lista (o return deve ser True or False)
print("Existe o código de rastreio JN426598255BR?", is_on_list("JN426598255BR", tracking_codes))
print("Existe o código de rastreio JN426598281BR?", is_on_list("JN426598281BR", tracking_codes))
print("Existe o código de rastreio NL00100010000?", is_on_list("NL00100010000", tracking_codes))

# Adicionar um código de rastreio na lista
add_tracking_code("JN426598295BR", tracking_codes)
add_tracking_code("JN426598834BR", tracking_codes)
add_tracking_code("JN426598851BR", tracking_codes)

# Remover um código de rastreio da lista
remove_tracking_code("JN426598247BR", tracking_codes)
remove_tracking_code("JN426598281BR", tracking_codes)

# Verificar se realmente foi removido da lista
print("Existe o código de rastreio JN426598247BR?", is_on_list("JN426598247BR", tracking_codes))
print("Existe o código de rastreio JN426598281BR?", is_on_list("JN426598281BR", tracking_codes))

# Consultar/Ler o tracking code de uma posição (indice) X na lista
print("O código na segunda posição: ", get_tracking_code(1, tracking_codes))
print("O código na quinta posição:", get_tracking_code(4, tracking_codes))

### WOW! Nossa empresa acabou de comprar uma outra empresa.
### Esta outra empresa também possui uma lista de tracking_codes de pedidos.
company_two_tracking_codes = ["JN426599534BR","JN426599525BR","JN426599517BR","JN426598370BR","JN426598410BR","JN426599401BR"]

# Primeiro vou usar a funcão sum_two_lists e passar as duas listas para ver o tamanho total delas juntas
print("O tamanho das 2 listas juntas é: ", sum_two_lists(tracking_codes, company_two_tracking_codes))

# Agora usando a função join_two_lists vou salvar na variavel lists_together o concacetanação/junção das listas.
lists_together = join_two_lists(tracking_codes, company_two_tracking_codes)

# Vou apenas printar pra ver como ficou:
print(lists_together)


#### Estamos indo bem! :)
#### Aproveitando, tem uma outra tarefa que preciso fazer também...

# Tenho aqui um Tuple com o valor das últimas vendas da empresa:
last_sales = (12.29, 1997.00, 98.50, 147.00, 1997.00, 700.50, 1000.00, 190.20, 1.99, 1997.00)

# Usando a função get_the_biggest quero descobrir o maior valor presente na lista:
print("Nas últimas vendas o maior valor é: ", get_the_biggest(last_sales))

## O produto mais caro é 1997.00 e quero saber quantas vezes ele aparece na lista das últimas vendas.
## Para isso vou usar a função count_in_list
print("O valor 1997.00 aparece: ", count_in_list(1997.00, last_sales) , " vezes na lista")

## E por último, para saber quanto a empresa vendeu, vou usar a função sum_total pra somar todos os valores presentes na lista:
print("Faturamento total da empresa ", sum_total(last_sales))

print("you reached to the and congradillations")