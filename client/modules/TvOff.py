import re
import RPi.GPIO as GPIO
import time
import requests
import subprocess
from py_irsend import irsend

WORDS = ["TV", "OFF"]

def handle(text, mic, profile):
    irsend.send_once('/home/pi/lircd.conf', ['KEY_POWER'])
    message = "turning off television"
    mic.say(message)

    payload = {'status':'tv off'}
    r = requests.post("http://178.128.62.29/api/device/tvoff", params=payload)

def isValid(text):
	return bool(re.search(r'\b(turn off tv|turn off the tv|tv off)\b', text, re.IGNORECASE))
