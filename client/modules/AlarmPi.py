# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time,timedelta
import os
import glob
import sys
from word2number import w2n

WORDS = []

def possibleinput(alarm):
    global i
    global clock
    global clockformat
    if "every" in alarm.lower():
        i = 1
    if "everyday" in alarm.lower():
        i = 1
    if "today" in alarm.lower():
        i = 0
    if "tomorrow" in alarm.lower():
        i = 0    
    if " A.M." in alarm:
        if ":" in alarm:
            clock = re.split(' AT |:| A.M.',alarm)
            clockformat = " AM"
            hour = clock[1]
            minute = clock[2]
        else:
            clock = re.split(r' AT |\s|',alarm)
            clockformat = " AM"
            hour = w2n.word_to_num(clock[i+1])
            if "A.M." in clock[i+3]:
                minute = w2n.word_to_num(clock[i+2])
            else:
                minute = w2n.word_to_num(clock[i+2])+w2n.word_to_num(clock[i+3])
    elif " P.M." in alarm:
        if ":" in alarm:
            clock = re.split(r' AT |:| P.M.',alarm)
            clockformat = " PM"
            hour = clock[1]
            minute = clock[2]
        else:
            clock = re.split(r' AT |\s',alarm)
            clockformat = " PM"
            hour = w2n.word_to_num(clock[i+1])
            if "P.M." in clock[i+3]:
                minute = w2n.word_to_num(clock[i+2])
            else:
                minute = w2n.word_to_num(clock[i+2])+w2n.word_to_num(clock[i+3])
        if i == 1:
            hour = int(hour) + 12
    if i == 1:
        return (hour,minute)
    elif i == 0:
        return (hour,minute,clockformat)

def handle(text, mic, profile):
    mic.say("What time did you want the alarm?")
    alarm = mic.activeListen()
    
    cronString = 'echo "'

    alarm.replace("at  ","",1)
    global weekdayString
    global hour
    global minute
    global hourString

    if "every" in alarm.lower():

        if "monday" in alarm.lower():
            alarm.replace("monday","",1)     
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 1"
            weekdayString = "Monday"

        elif "tuesday" in alarm.lower():
            alarm.replace("wednesday","",1)
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 2"
            weekdayString = "Tuesday"

        elif "wednesday" in alarm.lower():
            alarm.replace("wednesday","",1)
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 3"
            weekdayString = "Wednesday"

        elif "thursday" in alarm.lower():
            alarm.replace("thursday","",1)
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 4"
            weekdayString = "Thursday"

        elif "friday" in alarm.lower():
            alarm.replace("friday","",1)
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 5"
            weekdayString = "Friday"

        elif "saturday" in alarm.lower():  
            alarm.replace("saturday","",1)
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 6"
            weekdayString = "Saturday"

        elif "sunday" in alarm.lower():
            alarm.replace("sunday","",1)
            hour, minute = possibleinput(alarm)
            cronString += str(minute)+" "+str(hour)+" * * 0"
            weekdayString = "Sunday"

        else :
            sys.exit(1)

        cronString += ' /home/pi/.jasper/alarmScript.sh" | tee -a /var/spool/cron/crontabs/pi'
        print("cd /home/pi && "+cronString)

        if int(hour) > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString = str(hourInt)+" pm"
        else:
            hourString = str(hour)+ " am"

        print("Setting alarm for " + weekdayString +" at "+ hourString)

        os.system("cd /home/pi && "+cronString)

    elif "today" in alarm.lower():
        command ='echo "/home/pi/.jasper/alarmScript.sh" | at ' 
        hour, minute, clockformat = possibleinput(alarm)
        command += str(hour)
        command += ":"
        command += str(minute)
        command += clockformat
        print(command)
        os.system(command)
        
        xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
        print("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")
    
    elif "everyday" in alarm.lower():
        hour, minute = possibleinput(alarm)
        cronString += str(minute)+" "+str(hour)+" * * *"
        cronString += ' /home/pi/.jasper/alarmScript.sh" | tee -a /var/spool/cron/crontabs/pi'
        print("cd /home/pi && "+cronString)

        if hour > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString = str(hourInt)+" pm"
        else:
            hourString = str(hour)+ " am"

        print("Setting alarm everyday " +" at "+ hourString)

        os.system("cd /home/pi && "+cronString)

    elif "tomorrow" in alarm.lower():
        command ='echo "/home/pi/.jasper/alarmScript.sh" | at ' 
        hour, minute, clockformat = possibleinput(alarm)
        command += str(hour)
        command += ":"
        command += str(minute)
        command += clockformat
        command += " tomorrow"
        print(command)
        os.system(command)
        
        xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
        print("I set your alarm for tomorrow at "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")

def isValid(text):
    return bool(re.search(r'\b(((add|set) (a|another|an) (alarm|clock)|wake me))\b', text, re.IGNORECASE))
