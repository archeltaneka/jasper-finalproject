import thread
import time
import requests
import RPi.GPIO as GPIO

def check_light_status(threadName, delay):
    count = 0
    while count < float('inf'):
        r = requests.get('http://178.128.62.29/api/device/stat')
        data = r.json()
        time.sleep(delay)
        count += 1
        if data['light']['status'] == 'Light on':
##            GPIO.setmode(GPIO.BCM)
##            GPIO.setup(18, GPIO.OUT)
##            GPIO.output(18, GPIO.HIGH)
            print("Light on!")
        else:
##            GPIO.setmode(GPIO.BCM)
##            GPIO.output(18, GPIO.LOW)
##            GPIO.cleanup()
            print("Light off!")

check_light_status("Light: ", 4)

