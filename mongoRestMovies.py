from flask import Flask, jsonify, request, render_template
import pymongo 
import re

def connectToMongoDB():
    myClient = pymongo.MongoClient("mongodb://mongo:27017/unicode_decode_error_handler='ignore'")
    myDB = myClient["restMovies"]
    return myDB


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
myDB = connectToMongoDB()

@app.route('/form/')
def showInsertForm():
    return render_template('form.html')


@app.route('/movies/', methods=['GET'])
def getMovies():
    moviesCollection = myDB["movies"]
    moviesList = moviesCollection.find()
    movies = []
    for movie in moviesList:
        movie['_id'] = str(movie['_id'])
        movies.append(movie)
    data_dict = {"movies": movies}
    return jsonify(data_dict)

@app.route('/movies/actor/<string:actor>', methods=['GET'])
def getMoviesByActor(actor):
    moviesCollection = myDB["movies"]
    query = {"cast": actor}
    moviesList = moviesCollection.find(query)
    movies = []
    for movie in moviesList:
        movie['_id'] = str(movie['_id'])
        movies.append(movie)
    data_dict = {"movies": movies}
    return jsonify(data_dict)

@app.route('/movies/country/<string:country>', methods=['GET'])
def getMoviesByCountry(country):
    moviesCollection = myDB["movies"]
    regex_pattern = re.compile(f".*{re.escape(country)}.*", re.IGNORECASE)
    query = {"countries": {"$regex": regex_pattern}}
    moviesList = moviesCollection.find(query)
    movies = []
    for movie in moviesList:
        movie['_id'] = str(movie['_id'])
        movies.append(movie)
    data_dict = {"movies": movies}
    return jsonify(data_dict)
'''
Esta es la versión en la que el parámetro debe coincidir exactamente con el valor en la base de datos
@app.route('/movies/country/<string:country>', methods=['GET'])
def getMoviesByCountry(country):
    moviesCollection = myDB["movies"]
    query = {"countries": country}
    moviesList = moviesCollection.find(query)
    movies = []
    for movie in moviesList:
        movie['_id'] = str(movie['_id'])
        movies.append(movie)
    data_dict = {"movies": movies}
    return jsonify(data_dict)
'''
@app.route('/movies/runtime/lessthan/<int:runtime>', methods=['GET'])
def getMoviesByLessDuration(runtime):
    moviesCollection = myDB["movies"]
    query = {"runtime": { "$lt": runtime}}
    moviesList = moviesCollection.find(query)
    movies = []
    for movie in moviesList:
        movie['_id'] = str(movie['_id'])
        movies.append(movie)
    data_dict = {"movies": movies}
    return jsonify(data_dict)


@app.route('/movies/create', methods=['POST'])
def createMovie():
    myDB = connectToMongoDB()
    moviesCollection = myDB["movies"]
    content_type = request.headers.get('Content-Type')

    if (content_type == 'application/json'):
        jsonBody = request.json
        result = moviesCollection.insert_one(jsonBody)
        if result.acknowledged:
            successfulInsertionMessage = str(result.inserted_id)
            print(successfulInsertionMessage)
            response_data = {"inserteId": successfulInsertionMessage }
        else:
            response_data = {"message": "Error al insertar el documento"}
        
        # Devuelve una respuesta en formato JSON
        return jsonify(response_data)
    else:
        return 'Content-Type not accepted'








if __name__ == '__main__':
    '''app.run(port=4000)'''
    app.run(host='0.0.0.0', port=4000)
