import requests
 
api_url = 'http://10.113.1.111:8090/solucoes/categorias'

def get():
    
    response = requests.get(api_url)
    print(response.json())
 
def insert():
    api_url = 'http://10.113.1.111:8090/solucoes/categorias'
    categorias = {"nome_categoria": "Calça", "descricao": "cor Azul Masculino"}
    response = requests.post(api_url, json=categorias)
    print(response.json())

def update(id_categoria):
  rest = {"nome_categoria": "celular", "descricao":"Eletronicos"}
  response = requests.put(f'http://10.113.1.111:8090/solucoes/categorias_edit/{id_categoria}', json=rest)
  print(response)

def delete():
    api_url = "http://10.113.1.111:8090/solucoes/categorias/delete/1"
    response = requests.delete(api_url)
    print(response)

def delete():
    api_url = "http://10.113.1.111:8090/solucoes/produtos/delete/1"
    response = requests.delete(api_url)
    print(response)

#get()
insert()
get()
#update(1)
#delete(id)