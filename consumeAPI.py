import requests
import codecs
from flask import jsonify

response = requests.get("http://localhost:4000/movies/")

cadena_con_escape = response.text
cadena_decodificada = codecs.decode(cadena_con_escape, 'unicode-escape')

print(response.text)

response2 = requests.get("http://localhost:4000/movies/Alejandra Flechner")

cadena_con_escape = response2.text
cadena_decodificada = codecs.decode(cadena_con_escape, 'unicode-escape')

print(response2.text)


