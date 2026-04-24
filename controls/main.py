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

import RPi.GPIO as GPIO
from time import sleep
from enum import Enum

GPIO.setmode(GPIO.BCM)

MOTORPIN = 27
REVERSEPIN = 22
GPIO.setup(MOTORPIN, GPIO.OUT)
GPIO.setup(REVERSEPIN, GPIO.OUT)

def drivelm(direction):
    drive_motor(direction, MOTORPIN, REVERSEPIN)

# direction is a list of motor ports, first one is the forward and second one is reverse
# e.g. drive_motor([MOTORPIN, REVERSEPIN])
def drive_motor(direction):
    GPIO.output(direction[0], GPIO.HIGH)
    GPIO.output(direction[1], GPIO.LOW)

# direction here is an abuse of notation for the sake of convenience
def stop_motor(direction):	
    GPIO.output(direction[0], GPIO.LOW)
    GPIO.output(direction[1], GPIO.LOW)

