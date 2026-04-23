# temporary file probably
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

MOTORPIN = 27
REVERSEPIN = 22
GPIO.setup(MOTORPIN, GPIO.OUT)
GPIO.setup(REVERSEPIN, GPIO.OUT)

def drivelm(direction):
    drive_motor(direction, MOTORPIN, REVERSEPIN)

def drive_motor(direction, MOTORPIN, REVERSEPIN):
    if direction == 1:
        GPIO.output(MOTORPIN, GPIO.HIGH)
        GPIO.output(REVERSEPIN, GPIO.LOW)
    elif direction == -1:
        GPIO.output(MOTORPIN, GPIO.LOW)
        GPIO.output(REVERSEPIN, GPIO.HIGH)
    else:
        GPIO.output(MOTORPIN, GPIO.LOW)
        GPIO.output(REVERSEPIN, GPIO.LOW)

#while True:
#    drivelm(1)
#    sleep(1)
#    drivelm(-1)
#    sleep(1)
drivelm(0)

