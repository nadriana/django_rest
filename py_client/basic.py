import requests

#endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" # es lo mismo que http://127.0.0.1:8000/ 

get_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello world"}) # HTTP request
# print(get_response.text) #esto regresa el source code de la página
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JSON: JavaScript Object Notation ~ Python dictionary
print(get_response.json()) # this returns a Python dict
#print(get_response.status_code)

 