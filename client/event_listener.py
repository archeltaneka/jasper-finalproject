import thread
import time
import requests
import subprocess
import RPi.GPIO as GPIO

def check_light_status(threadName, delay):
    count = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    while count < float('inf'):
        r = requests.get('http://178.128.62.29/api/device/stat')
        data = r.json()
        time.sleep(delay)
        count += 1
        if data['light']['status'] == 'light on':
            GPIO.output(18, GPIO.HIGH)
            print('Light on!')
        if data['light']['status'] == 'light off':
            GPIO.output(18, GPIO.LOW)
##            GPIO.cleanup()
            print('Light off!')
        if data['tv']['status'] == 'tv on' or data['tv']['status'] == 'tv off':
            rtn = subprocess.call(["irsend", "SEND_ONCE", "/home/pi/lircd.conf", "KEY_POWER"])

check_light_status("Device", 1)

