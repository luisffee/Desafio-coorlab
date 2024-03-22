from flask import Flask, request,jsonify
from flask_cors import CORS
from db import InitDB, Companies, Cities, Transports

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://coorlab:coorlab@localhost/transports'
app.app_context().push()
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'secret'

db = InitDB(app).start()

def transportSerializer(transport):
    return {
        'name': transport.name,
        'price_confort': transport.price_confort,
        'price_econ': transport.price_econ,
        'city': transport.city,
        'duration': transport.duration,
        'seat': transport.seat,
        'bed': transport.bed
	}

def citySerializer(cities):
    return {
        'cities': [city.city for city in cities]
    }

@app.route('/api/transports', methods=['GET','POST'])
def getData():
    transports = Transports.query.order_by(Transports.id.asc()).all()
    transp_list = []
    for transport in transports:
        transp_list.append(transportSerializer(transport))
    #print(transp_list)
    return jsonify(transp_list)

@app.route('/api/transports/<int:id>', methods=['GET'])
def getDataByID(id):
    transport = Transports.query.filter_by(id=id).one()
    formatted_transport = transportSerializer(transport)
    return jsonify(formatted_transport)

@app.route('/api/transports/cities', methods=['GET'])
def getCities():
    cities = Cities.query.order_by(Cities.id.asc()).all()
    return jsonify(citySerializer(cities))

if __name__ == '__main__':
	app.run(debug=True, port=3000)