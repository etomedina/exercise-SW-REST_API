"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os, requests
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Person, Planet, Vehicle
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# @app.route('/user', methods=['GET'])
# def handle_hello():

#     response_body = {
#         "msg": "Hello, this is your GET /user response "
#     }

#     return jsonify(response_body), 200

# @app.route('/people2', methods=['GET'])
# def get_people():
#     requests.get('https://www.swapi.tech/api/')
#     return 

#poblar base de dato de personajes
base_url = "https://www.swapi.tech/api/"
@app.route('/poblar-personaje', methods=['GET'])
def get_poblar_personaje():
    response =  requests.get(f"{base_url}{'people'}/?page=1")
    results = response.json()['results']
    count = 0 
    for xdict in results:
        response = requests.get(xdict['url'])
        detaresponse = response.json()['result']['properties']
        person = Person.created(**detaresponse) 
        if person != None:
            count = count  + 1
    return jsonify({'count':count}),200

#poblar base de dato de planetas
@app.route('/poblar-planeta', methods=['GET'])
def get_poblar_planeta():
    response =  requests.get(f"{base_url}{'planets'}/?page=1")
    results = response.json()['results']
    count = 0 
    for xdict in results:
        response = requests.get(xdict['url'])
        detaresponse = response.json()['result']['properties']
        planet = Planet.created(**detaresponse) 
        if planet != None:
            count = count  + 1
    return jsonify({'count':count}),200

#poblar base de datos de vehiculos
@app.route('/poblar-vehiculo', methods=['GET'])
def get_poblar_vehiculo():
    response =  requests.get(f"{base_url}{'vehicles'}/?page=1")
    results = response.json()['results']
    count = 0 
    for xdict in results:
        response = requests.get(xdict['url'])
        detaresponse = response.json()['result']['properties']
        vehicle = Vehicle.created(**detaresponse) 
        if vehicle != None:
            count = count  + 1
    return jsonify({'count':count}),200


#1. obtener people
@app.route('/people', methods=['GET'])
def get_all_people():
    people= Person.query.all()
    list_people= list(map(
        lambda item: item.serialize(), people))
    return jsonify(list_people),200


#2. obtener people/especifica
@app.route('/people/<int:id>', methods=['GET'])
def more_details_person(id):
    #buscar en base de datos al pesonaje cuya id corresponde a la suya
    person = Person.query.get(id)
    if isinstance(person,Person):
        #enviar vista detallada del personaje 
        dictionary = person.serialize(long=True)
        return jsonify(dictionary),200
    return 404

#3. obtener planetas
@app.route('/planets', methods=['GET'])
def get_all_planets():
    planets= Planet.query.all()
    list_planets= list(map(
        lambda item: item.serialize(), planets))
    return jsonify(list_planets),200

#4. obtener planetas/especificos
@app.route('/planet/<int:id>', methods=['GET'])
def more_details_planet(id):
    #buscar en base de datos del planeta cuya id corresponde a la suya
    planet = Planet.query.get(id)
    if isinstance(planet,Planet):
        #enviar vista detallada del planeta
        dictionary = planet.serialize(long=True)
        return jsonify(dictionary),200
    return 404

#5. obtener usuarios
@app.route('/user', methods=['GET'])
def get_all_user():
    users= User.query.all()
    list_users= list(map(
        lambda item: item.serialize(), users))
    return jsonify(list_users),200

#6. obtener usuarios/favoritos

#7. postear favorito, planeta por su id

#8. postear favorito, people por su id


#9. borrar favorito, planeta por su id

#10. borrar favorito, people por su id



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
