#!/usr/bin/env python3
from gpiozero import *
from time import sleep

LMOTORPIN = 27
LREVERSEPIN = 22

RMOTORPIN = 23
RREVERSEPIN = 24

lm = Motor(forward=LMOTORPIN, backward=LREVERSEPIN, pwm=True)
rm = Motor(forward=RMOTORPIN, backward=RREVERSEPIN, pwm=True)

motors = [lm, rm]

def drive_motor(motor, speed):
	s = abs(speed)
	if speed > 0:
		motor.forward(speed=abs(s))
	else:
		motor.backward(speed=abs(s))

# argument order: list(lm, rm), list(lstick, rstick)
def arcade(dir):
	lraw = (dir[0] - dir[1])/2
	rraw = (dir[0] + dir[1])/2
	
	# hack
	if lraw > 1:
		lraw = 1
	elif lraw < -1:
		lraw = -1
	if rraw > 1:
		rraw = 1
	elif rraw < -1:
		rraw = -1

	drive_motor(motors[0], lraw)
	drive_motor(motors[1], rraw)
