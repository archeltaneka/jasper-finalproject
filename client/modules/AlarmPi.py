# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time,timedelta
import os
import glob
import sys
from word2number import w2n

WORDS = []

def handle(text, mic, profile):
    mic.say("What time did you want the alarm?")
    alarm = mic.activeListen()
    
    cronString = 'echo "'

    alarm.replace("at  ","",1)
    global weekdayString
    global hour
    global clock
    global clockformat
    global hourString

    if "every" in alarm.lower():

        if "monday" in alarm.lower():
            alarm.replace("monday","",1)     
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 1"
            weekdayString = "Monday"

        elif "tuesday" in alarm.lower():
            alarm.replace("wednesday","",1)
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 3"
            weekdayString = "Tuesday"

        elif "wednesday" in alarm.lower():
            alarm.replace("wednesday","",1)
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 3"
            weekdayString = "Wednesday"

        elif "thursday" in alarm.lower():
            alarm.replace("thursday","",1)
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 4"
            weekdayString = "Thursday"

        elif "friday" in alarm.lower():
            alarm.replace("friday","",1)
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 5"
            weekdayString = "Friday"

        elif "saturday" in alarm.lower():  
            alarm.replace("saturday","",1)
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 6"
            weekdayString = "Saturday"

        elif "sunday" in alarm.lower():
            alarm.replace("sunday","",1)
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 0"
            weekdayString = "Sunday"

        else :
            sys.exit(1)

        cronString += ' /home/pi/.jasper/alarmScript.sh" | tee -a /var/spool/cron/crontabs/pi'
        print("cd /home/pi && "+cronString)

        if hour > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString = str(hourInt)+" pm"
        else:
            hourString = str(hour)+ " am"

        mic.say("Setting alarm for " + weekdayString +" at "+ hourString)

        os.system("cd /home/pi && "+cronString)

    elif "today" in alarm.lower():
        command ='echo "/home/pi/.jasper/alarmScript.sh" | at ' 
        if "a.m." in alarm.lower():
            clock = re.split(' AT |:| A.M.',alarm)
            clockformat = " AM"
        elif "p.m." in alarm.lower():
            clock = re.split(' AT |:| P.M.',alarm)
            clockformat = " PM"
        clock = re.split(' AT |:| P.M.',alarm)
        command += str(clock[1])
        command += ":"
        command += str(clock[2])
        command += clockformat
        print(command)
        os.system(command)
        
        xHoursFromNow = datetime.now() + timedelta(hours=int(clock[1]))
        mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.clock[2])+". ")
    
    elif "everyday" in alarm.lower():
        if "a.m." in alarm.lower():
            clock = re.split(' AT |:| A.M.',alarm)
            hour = clock[1]
        elif "p.m." in alarm.lower():
            clock = re.split(' AT |:| P.M.',alarm)
            hour = int(clock[1])+12
        cronString += str(clock[2])+" "+str(hour)+" * * *"
        cronString += ' /home/pi/.jasper/alarmScript.sh" | tee -a /var/spool/cron/crontabs/pi'
        print("cd /home/pi && "+cronString)

        if hour > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString = str(hourInt)+" pm"
        else:
            hourString = str(hour)+ " am"

        mic.say("Setting alarm everyday " +" at "+ hourString)

        os.system("cd /home/pi && "+cronString)

    elif "tomorrow" in alarm.lower():
        command ='echo "/home/pi/.jasper/alarmScript.sh" | at ' 
        if "a.m." in alarm.lower():
            clock = re.split(' AT |:| A.M.',alarm)
            clockformat = " AM"
        elif "p.m." in alarm.lower():
            clock = re.split(' AT |:| P.M.',alarm)
            clockformat = " PM"
        clock = re.split(' AT |:| P.M.',alarm)
        command += str(clock[1])
        command += ":"
        command += str(clock[2])
        command += clockformat
        command += " tomorrow"
        print(command)
        os.system(command)
        
        xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
        mic.say("I set your alarm for tomorrow at "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.clock[2])+". ")

def isValid(text):
    return bool(re.search(r'\b(((add|set) (a|another|an) (alarm|clock)|wake me))\b', text, re.IGNORECASE))
