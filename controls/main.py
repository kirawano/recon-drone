#!/usr/bin/env python3

from flask import *
from time import sleep
from markupsafe import escape

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
    print(d['ctrl'])
    return jsonify({"success":"true"})


def get_dirs():
	return d

from gpiozero import *
from time import sleep

MOTORPIN = 27
REVERSEPIN = 22

# e.g. lm.forward(speed=0.5)
lm = Motor(forward=MOTORPIN, backward=REVERSEPIN, pwm=True)

def drive_motor(motor, speed):
	s = abs(speed)
	if speed > 0:
		motor.forward(speed=s)
	else:
		motor.backward(speed=s)
