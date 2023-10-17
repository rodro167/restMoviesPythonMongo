import pymongo 
import pandas as pd
import json

def row_to_json(row):
    # Verificar si una celda contiene una lista separada por comas
    for col in row.index:
        if isinstance(row[col], str) and ',' in row[col]:
            # Dividir la cadena en elementos individuales y convertirlo en una lista
            row[col] = row[col].split(',')
    # Convertir la fila en JSON
    return row.to_json()

df = pd.read_excel('Sheets/Movies.xlsx')
json_list = df.apply(row_to_json, axis=1)

myClient = pymongo.MongoClient("mongodb://localhost:27017/")
myDB = myClient["restMovies"]
myCollection = myDB["movies"]


documents = []

for json_str in json_list:
    document = json.loads(json_str)
    documents.append(document)
    print(document)
    
myCollection.insert_many(documents)