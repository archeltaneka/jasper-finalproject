import re
import RPi.GPIO as GPIO
import time
import requests

WORDS = ["LIGHT OFF", "LIGHTS OFF", "TURN OFF THE LIGHT", "TURN OFF LIGHT"]


def handle(text, mic, profile):

	GPIO.setmode(GPIO.BCM)
	
	GPIO.output(18, GPIO.LOW)
	GPIO.cleanup()

	#suruh jasper jwb lampunya ud nyala
	message = "Light off"
	mic.say(message)
	# POST light status here
	payload = {'status': 'light off'}
	r = requests.post("http://178.128.62.29/api/device/lightoff", params=payload)

def isValid(text):
##	return bool(re.search(r'\b(turn off light|turn off the light|light off|lights off)\b', text, re.IGNORECASE))
        return any(word in text.upper() for word in WORDS)
