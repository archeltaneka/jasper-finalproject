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
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
                    cronString += str(minute)+" "+str(hour)+" * * 1"
                    weekdayString = "Monday"

            elif "tuesday" in alarm.lower():
                    alarm.replace("wednesday","",1)
                    clock = re.split(' at |:',alarm)
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
                    cronString += str(minute)+" "+str(hour)+" * * 3"
                    weekdayString = "Wednesday"

            elif "wednesday" in alarm.lower():
                    alarm.replace("wednesday","",1)
                    clock = re.split(' at |:',alarm)
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
                    cronString += str(minute)+" "+str(hour)+" * * 3"
                    weekdayString = "Wednesday"

            elif "thursday" in alarm.lower():
                    alarm.replace("thursday","",1)
                    clock = re.split(' at |:',alarm)
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
                    cronString += str(minute)+" "+str(hour)+" * * 4"
                    weekdayString = "Thursday"

            elif "friday" in alarm.lower():
                    alarm.replace("friday","",1)
                    clock = re.split(' at |:',alarm)
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
                    cronString += str(minute)+" "+str(hour)+" * * 5"
                    weekdayString = "Friday"

            elif "saturday" in alarm.lower():  
                    alarm.replace("saturday","",1)
                    clock = re.split(' at |:',alarm)
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
                    cronString += str(minute)+" "+str(hour)+" * * 6"
                    weekdayString = "Saturday"

            elif "sunday" in alarm.lower():
                    alarm.replace("sunday","",1)
                    clock = re.split(' at |:',alarm)
                    if (clock[1].isdigit):
                        hour = clock[1]
                    else:
                        hour = w2n.word_to_num(clock[1])
                    if (clock[2].isdigit):
                        minute = clock[2]
                    else:
                        minute = w2n.word_to_num(clock[2])
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
            if (clock[1].isalpha):
                    command += str(w2n.word_to_num(clock[1]))
            else:
                    command += str(clock[1])
            command += ":"
            if "am" in alarm:
                onlynum = re.sub(" am","",clock[2])
            elif "AM" in alarm:
                onlynum = re.sub(" AM","",clock[2])
            elif "pm" in alarm:
                onlynum = re.sub(" pm","",clock[2])
            elif "PM" in alarm:
                onlynum = re.sub(" PM","",clock[2])
            if (onlynum.isalpha):
                    command += str(w2n.word_to_num(onlynum))
            else:
                    command += str(onlynum)
            if "am" in alarm.lower():
                clock[2].replace("am","",1)
                command += " AM"
            elif "pm" in alarm.lower():
                clock[2].replace("pm","",1)
                command += " PM"
            print(command)
            os.system(command)
            
            xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
            mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")

def isValid(text):
    return bool(re.search(r'\b(((add|set) (a|another|an) (alarm|clock)|wake me))\b', text, re.IGNORECASE))
