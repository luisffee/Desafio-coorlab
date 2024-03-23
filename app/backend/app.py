from flask import Flask, request,jsonify
from flask_cors import CORS
from db import InitDB, Companies, Cities, Travels

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://coorlab:coorlab@localhost/transports'
app.app_context().push()
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'secret'

db = InitDB(app).start()

def Travelserializer(transport):
    return {
        'name': transport.name.name,
        'price_confort': transport.price_confort,
        'price_econ': transport.price_econ,
        'city': transport.city.city,
        'duration': transport.duration,
        'seat': transport.seat,
        'bed': transport.bed
	}

def citySerializer(cities):
    serialized = {}
    for tuples in cities:
        serialized[tuples[0]] = tuples[1]
    return {
        'cities': serialized
    }

@app.route('/api/Travels', methods=['GET','POST'])
def getData():
    Travels = Travels.query.order_by(Travels.id.asc()).all()
    transp_list = []
    for transport in Travels:
        transp_list.append(Travelserializer(transport))
    return jsonify(transp_list)

@app.route('/api/Travels/<int:id>', methods=['GET'])
def getDataByID(id):
    transport = Travels.query.filter_by(id=id).one()
    formatted_transport = Travelserializer(transport)
    return jsonify(formatted_transport)

@app.route('/api/Travels/bestprices/<int:city_id>', methods=['GET'])
def getBestPrices(city_id):
    best_price_econ = Travels.query.filter(Travels.city_id==city_id).order_by(Travels.price_econ.asc(), Travels.duration.asc()).first()
    best_price_confort = Travels.query.filter(Travels.city_id==city_id).order_by(Travels.duration.asc(), Travels.price_confort.asc()).first()
    serialized_data = {
        'best_price_econ': Travelserializer(best_price_econ),
        'best_price_confort': Travelserializer(best_price_confort)
    }
    return jsonify(serialized_data)

@app.route('/api/Travels/cities', methods=['GET'])
def getCities():
    cities = Cities.query.with_entities(Cities.id, Cities.city).order_by(Cities.id.asc()).all()
    return jsonify(citySerializer(cities))

if __name__ == '__main__':
	app.run(debug=True, port=3000)