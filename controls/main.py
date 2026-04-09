#!/usr/bin/env python3

from flask import *
from time import sleep
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def root():
    url_for('static', filename='controls.js')
    print("hi")
    return render_template('index.html')

@app.route('/controller_data', methods=['POST'])
def controller():
    d = request.get_json()
    print(d)
    return jsonify({"success":"true"})
