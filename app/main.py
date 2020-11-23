from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return ("Hola Mundo, soy Python!")

@app.route('/bye')
def bye_world():
	return ("Adios mundo cruel")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

