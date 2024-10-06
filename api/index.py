from flask import Flask,jsonify
from api.months import questions

app = Flask(__name__)

@app.route('/')
def home():
    question = questions[0]
    to_return = question["April"]
    return jsonify(to_return)

@app.route('/about')
def about():
    return 'About'
