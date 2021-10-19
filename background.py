#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import json


while True:
  with open('led-pwm.txt', 'r') as f:
    data = json.load(f)
    pin = int(data['pin'])
    slide = int(data['slider1'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    pwm = GPIO.PWM(pin, 100)
    pwm.ChangeDutyCycle(slide)
    time.sleep(0.2)

  