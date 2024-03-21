from flask import Flask, request,jsonify
from flask_cors import CORS
from db import InitDB, Transports

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

@app.route('/api', methods=['POST','GET'])
def submitData():
	response_object = {'status':'success'}
	if request.method == 'POST':
		post_data = request.get_json()
		message = post_data.get('message')
		print(message)
		response_object['message'] = 'Message received!'
		return jsonify(response_object)

if __name__ == '__main__':
	app.run(debug=True, port=3000)