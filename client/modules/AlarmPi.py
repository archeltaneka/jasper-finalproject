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
<<<<<<< HEAD
            alarm.replace("monday","",1)
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 1"
||||||| merged common ancestors
            alarm.replace("monday","",1)
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 1"
=======
            alarm.replace("monday","",1)     
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 1"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
            weekdayString = "Monday"

        elif "tuesday" in alarm.lower():
            alarm.replace("wednesday","",1)
<<<<<<< HEAD
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 3"
||||||| merged common ancestors
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 3"
=======
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 3"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
            weekdayString = "Tuesday"

        elif "wednesday" in alarm.lower():
            alarm.replace("wednesday","",1)
<<<<<<< HEAD
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 3"
||||||| merged common ancestors
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 3"
=======
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 3"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
            weekdayString = "Wednesday"

        elif "thursday" in alarm.lower():
            alarm.replace("thursday","",1)
<<<<<<< HEAD
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 4"
||||||| merged common ancestors
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 4"
=======
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 4"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
            weekdayString = "Thursday"

        elif "friday" in alarm.lower():
            alarm.replace("friday","",1)
<<<<<<< HEAD
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 5"
||||||| merged common ancestors
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 5"
=======
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 5"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
            weekdayString = "Friday"

        elif "saturday" in alarm.lower():  
            alarm.replace("saturday","",1)
<<<<<<< HEAD
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 6"
||||||| merged common ancestors
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 6"
=======
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 6"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
            weekdayString = "Saturday"

        elif "sunday" in alarm.lower():
            alarm.replace("sunday","",1)
<<<<<<< HEAD
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
#                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 0"
||||||| merged common ancestors
            clock = re.split(' at |:',alarm)
            firsthour = clock[1]
            if "a.m." in alarm:
                minute = re.sub(" a.m.","",clock[2])
            elif "A.M." in alarm:
                minute = re.sub(" A.M.","",clock[2])
            elif "p.m." in alarm:
                minute = re.sub(" p.m.","",clock[2])
                hour = int(firsthour)+12
            elif "P.M." in alarm:
                minute = re.sub(" P.M.","",clock[2])
                hour = int(firsthour)+12
            cronString += str(minute)+" "+str(hour)+" * * 0"
=======
            if "a.m." in alarm.lower():
                clock = re.split(' AT |:| A.M.',alarm)
                hour = clock[1]
            elif "p.m." in alarm.lower():
                clock = re.split(' AT |:| P.M.',alarm)
                hour = int(clock[1])+12
            cronString += str(clock[2])+" "+str(hour)+" * * 0"
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
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
<<<<<<< HEAD
        clock = re.split(' AT |:| P.M.',alarm)
        command += clock[1]
        command += ":"
        if "a.m." in alarm:
            onlynum = re.sub(" a.m.","",clock[2])
        elif "A.M." in alarm:
            onlynum = re.sub(" A.M.","",clock[2])
        elif "p.m." in alarm:
            onlynum = re.sub(" p.m.","",clock[2])
 #       elif "P.M." in alarm:
 #           onlynum = re.sub(" P.M.","",clock[2])
        command += clock[2]
||||||| merged common ancestors
        clock = re.split(' at |:',alarm)
        command += str(clock[1])
        command += ":"
        if "a.m." in alarm:
            onlynum = re.sub(" a.m.","",clock[2])
        elif "A.M." in alarm:
            onlynum = re.sub(" A.M.","",clock[2])
        elif "p.m." in alarm:
            onlynum = re.sub(" p.m.","",clock[2])
        elif "P.M." in alarm:
            onlynum = re.sub(" P.M.","",clock[2])
        command += str(onlynum)
=======
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
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
        
<<<<<<< HEAD
        xHoursFromNow = datetime.now() + timedelta(hours=int(clock[1]))
        mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")
||||||| merged common ancestors
        xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
        mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")
=======
        xHoursFromNow = datetime.now() + timedelta(hours=int(clock[1]))
        mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.clock[2])+". ")
>>>>>>> ff9f5a1a9bc427b719e2e4f4a0b618e887aad5b6
    
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
