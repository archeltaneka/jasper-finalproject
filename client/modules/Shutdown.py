# -*- coding: utf-8-*-
import random
import re
import os
import subprocess

WORDS = ["SHUTDOWN", "SHUTDOWN", "BYE"]

PRIORITY = 3

def handle(text, mic, profile):
    """
        Shuts down the system
    """

    messages = ["Goodbye!", "See you later!", "Bye-bye"]
    message = random.choice(messages)
    mic.say(message)

    # Run the shutdown command --> sudo shutdown -f now
    command = "/usr/bin/sudo /sbin/shutdown -f now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.comunicate()[0]
    
def isValid(text):
    return any(word in text.upper() for word in WORDS)
