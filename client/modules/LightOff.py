import re
import RPi.GPIO as GPIO
import time

WORDS = ["TURN", "OFF", "LIGHT"]


def handle(text, mic, profile):

	GPIO.setmode(GPIO.BCM)
	
	GPIO.output(18, GPIO.LOW)
	GPIO.cleanup()

	#suruh jasper jwb lampunya ud nyala
	message = "light off"
	mic.say(message)
	# POST light status here
	payload = {'status': 'light off'}
	r = requests.post("http://127.0.0.1:5000/try", params=payload)

def isValid(text):
	return bool(re.search(r'\b(turn off light|turn off the light|light off|lights off)\b', text, re.IGNORECASE))
