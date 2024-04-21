from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo! Este es un ejemplo de aplicación web usando Flask.'

if __name__ == '__main__':
    app.run(debug=True)
