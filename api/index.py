from flask import Flask,jsonify
from months import questions

app = Flask(__name__)

@app.route('/')
def home():
    # question = questions[0]
    # to_return = question["April"]
    return "Its working"

@app.route('/about')
def about():
    return 'About'
