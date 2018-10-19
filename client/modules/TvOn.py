import re
import RPi.GPIO as GPIO
import time
import requests
import subprocess

WORDS = ["TV", "ON"]

def handle(text, mic, profile):
    rtn = subprocess.call(["irsend", "SEND_ONCE", "/home/pi/lircd.conf", "KEY_POWER"])
    message = "tv on"
    mic.say(message)

    payload = {'status':'tv on'}
    r = requests.post("http://178.128.62.29/api/device/tvon", params=payload)

def isValid(text):
	return bool(re.search(r'\b(turn on tv|turn on the tv|tv on)\b', text, re.IGNORECASE))
