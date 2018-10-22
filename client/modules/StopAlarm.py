# -*- coding: utf-8-*-
import random
import re
import os

WORDS = ['STOP']

def handle(text, mic, profile):
    command = "sudo sh /home/pi/.jasper/AlarmScriptShell/stop.sh"    
    os.system(command)

def isValid(text):
    return bool(re.search(r'\bstop alarm\b', text, re.IGNORECASE))
