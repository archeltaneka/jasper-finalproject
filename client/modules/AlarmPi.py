import datetime
import re
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = []

def wordstoint(words):
    value = ""

    if "one" in word.lower():
        value = "1"
    elif "two" in word.lower():
        value = "2"
    elif "three" in word.lower():
        value = "3"
    elif "four" in word.lower():
        value = "4"
    elif "five" in word.lower():
        value = "5"
    elif "six" in word.lower():
        value = "6"
    elif "seven" in word.lower():
        value = "7"
    elif "eight" in word.lower():
        value = "8"
    elif "nine" in word.lower():
        value = "9"
    elif "ten" in word.lower():
        value = "10"
    elif "eleven" in word.lower():
        value = "11"
    elif "twelve" in word.lower():
        value = "12"
    else :
	int_val = int(re.search(r'\d+', word).group())      
	value = str(int_val)

    if "pm" in word.lower() or "p.m." in word.lower():
        valueInt = int(value)
        valueInt += 12
        value = str(valueInt)
        
    return value

def handle(text,mic,profile):
    mic.say("when the alarm will be set?")
    text = mic.activeListen()
    hour = wordstoint(text)
    cronstring = 'echo "'
    cronstring 
    if hour > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString += str(hourInt)+" pm"
    	else:
            hourString +=str(hour)+ " am"
    mic.say("Setting alarm for " + " at " + hourString)
    os.system("cd /home/raspberry &&"+cronstring)
    
    

def isValid(text):
    return bool(re.search(r'\b(set|add) alarm\b)', text, re.IGNORECASE))