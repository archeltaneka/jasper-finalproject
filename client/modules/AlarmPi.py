import datetime
import re
import os
from client.app_utils import getTimezone
from semantic.dates import DateService
from word2number import w2n 

WORDS = []

def words_to_hour(word):

##    HOURS = {'ZERO':0, 'ONE':1, 'TWO':2, 'THREE':3, 'FOUR':4, 'FIVE':5,
##             'SIX': 6, 'SEVEN':7, 'EIGHT':8, 'NINE':9, 'TEN':10,
##             'ELEVEN':11, 'TWELVE':12, 'THIRTEEN':13, 'FOURTEEN':14, 'FIFTEEN':15,
##             'SIXTEEN':16, 'SEVENTEEN':17, 'EIGHTEEN':18, 'NINETEEN':19, 'TWENTY':20,
##             'TWENTY ONE':21, 'TWENTY TWO': 22, 'TWENTY THREE':23}
##
##    value = 0
##    for hours in HOURS:
##        if hours == word:
##            return 
    
##    value = ""
##
##    if "one" in word.lower():
##        value = "1"
##    elif "two" in word.lower():
##        value = "2"
##    elif "three" in word.lower():
##        value = "3"
##    elif "four" in word.lower():
##        value = "4"
##    elif "five" in word.lower():
##        value = "5"
##    elif "six" in word.lower():
##        value = "6"
##    elif "seven" in word.lower():
##        value = "7"
##    elif "eight" in word.lower():
##        value = "8"
##    elif "nine" in word.lower():
##        value = "9"
##    elif "ten" in word.lower():
##        value = "10"
##    elif "eleven" in word.lower():
##        value = "11"
##    elif "twelve" in word.lower():
##        value = "12"
##    else :
##	int_val = int(re.search(r'\d+', word).group())      
##	value = str(int_val)
##
##    if "pm" in word.lower() or "p.m." in word.lower():
##        valueInt = int(value)
##        valueInt += 12
##        value = str(valueInt)
##        
##    return value

def words_to_minute(word):

    MINUTES = {}

    value = 0
    for minute in MINUTES:
        if minute == word:
            return minute
        else:
            return 0


def handle(text,mic,profile):
    mic.say("what hour?")
    first = mic.activeListen()
    mic.say("what minute?")
    second = mic.activeListen()
    hour = w2n.word_to_num(first)
    minute = w2n.word_to_num(second)
    cronstring = 'echo "'
    cronstring += minute + hour+ " * * 3" # belom lengkap
    if hour > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString = str(hourInt)+" pm"
    else:
            hourString = str(hour)+ " am"
    
    mic.say("Setting alarm for " + " at " + hourString)
    os.system("cd /home/raspberry &&"+cronstring)
    
    

def isValid(text):
    return bool(re.search(r'\b(set|add) alarm\b)', text, re.IGNORECASE))
