from flask import Flask, request,jsonify,json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
Cors = CORS(app)
CORS(app, resources={r'/*': {'origins': '*'}},CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'secret'


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