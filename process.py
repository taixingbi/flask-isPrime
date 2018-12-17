from flask import Flask, render_template, request, jsonify
from demo import Prime  

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
	name = request.form['name']

	if not name:
		return jsonify({'error' : 'Please enter an integer'})

	if not name.isnumeric():
		return jsonify({'error' : 'This is not an integer'})

	ans= Prime( int(name) ).ans()

	return jsonify({'name' : ans})


if __name__ == '__main__':
	app.run(debug=True)