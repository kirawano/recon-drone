from flask import *
from time import sleep
from markupsafe import escape
from motor import arcade

app = Flask(__name__)

d = []

@app.route('/')
def root():
    url_for('static', filename='controls.js')
    print("hi")
    return render_template('index.html')

@app.route('/controller_data', methods=['POST'])
def controller():
    d = request.get_json()['ctrl']
    #drive_motor(rm, d[0])
    arcade(d)
    return jsonify({"success":"true"})


def get_dirs():
	return d
