from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Engr Emmanuel ELOKA is a BOSS....YES!!!!'
