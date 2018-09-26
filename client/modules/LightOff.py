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

def isValid(text):
	return bool(re.search(r'\b(turn off light)\b', text, re.IGNORECASE))
