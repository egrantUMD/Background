#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import json


while True:
  with open('led-pwm.txt', 'r') as f:
    data = json.load(f)
    p1 = int(data['PIN'])
    slide = int(data['slider1'])

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(p1, GPIO.OUT)

    pwm = GPIO.PWM(p1, 100)
    pwm.ChangeDutyCycle(slide)
    time.sleep(0.2)

  