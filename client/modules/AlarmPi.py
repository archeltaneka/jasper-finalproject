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
    global minute
    global clock
    global hourString

    if "every" in alarm.lower():

            if "monday" in alarm.lower():
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
                    weekdayString = "Monday"

            elif "tuesday" in alarm.lower():
                    alarm.replace("wednesday","",1)
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
                    weekdayString = "Wednesday"

            elif "wednesday" in alarm.lower():
                    alarm.replace("wednesday","",1)
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
                    weekdayString = "Wednesday"

            elif "thursday" in alarm.lower():
                    alarm.replace("thursday","",1)
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
                    weekdayString = "Thursday"

            elif "friday" in alarm.lower():
                    alarm.replace("friday","",1)
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
                    weekdayString = "Friday"

            elif "saturday" in alarm.lower():  
                    alarm.replace("saturday","",1)
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
                    weekdayString = "Saturday"

            elif "sunday" in alarm.lower():
                    alarm.replace("sunday","",1)
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
            if "a.m." in alarm.lower():
                command += " AM"
            elif "p.m." in alarm.lower():
                command += " PM"
            print(command)
            os.system(command)
            
            xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
            mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")

def isValid(text):
    return bool(re.search(r'\b(((add|set) (a|another|an) (alarm|clock)|wake me))\b', text, re.IGNORECASE))
