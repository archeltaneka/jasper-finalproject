from flask import Flask, render_template, jsonify
import re
import RPi.GPIO as GPIO
import time
import requests

WORDS = ["TURN", "ON", "LIGHT"]

def handle(text, mic, profile):

	GPIO.setmode(GPIO.BCM)
	
	#setting up the pin to be a pin that outputs information
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, GPIO.HIGH) #kita pake GPIO18
	
	#yg ini bisa buat off kayaknya
	#time.sleep(3) #lamp on only for 3 seconds
	#GPIO.output(18, GPIO.LOW)
	#GPIO.cleanup()

	#suruh jasper jwb lampunya ud nyala
	message = "light on"
	mic.say(message)

	# POST light status here
	message = {'status': 'Light on'}
	r = requests.post("http://178.128.62.29/api/device/lighton", params=message)

def isValid(text):
	return bool(re.search(r'\b(turn on light|turn on the light|light on|lights on)\b', text, re.IGNORECASE))
