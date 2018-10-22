import re
import RPi.GPIO as GPIO
import time
import requests
import subprocess
from py_irsend import irsend

WORDS = ["TURN ON TV", "TURN ON THE TV", "TV ON", "TV", "TELEVISION"]

def handle(text, mic, profile):
    irsend.send_once('/home/pi/lircd.conf', ['KEY_POWER'])
    message = "turning on television"
    mic.say(message)

    payload = {'status':'tv on'}
    r = requests.post("http://178.128.62.29/api/device/tvon", params=payload)

def isValid(text):
##	return bool(re.search(r'\b(turn on tv|turn on the tv|tv on)\b', text, re.IGNORECASE))
        return any(word in text.upper() for word in WORDS)
