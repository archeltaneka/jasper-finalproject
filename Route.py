from flask import Flask, render_template, jsonify
import datetime
import re
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

#open in http://127.0.0.1:5000/
@app.route('/')
def hello():
    return 'Hello world'

#kalo mau test pake html file
#https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/6
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/lightOn")
def lightOn():
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(18, GPIO.OUT)
		GPIO.output(18, GPIO.HIGH) 
		response = {"status": "light on"}

   	except:
      		response = {"status": "failed turning light on"}

   	#templateData = {
      	#	'response' : response
      	#}

   	#return render_template('main.html', **templateData)
	return jsonify(response)

@app.route("/lightOff")
def lightOff():
	try:
		GPIO.setmode(GPIO.BCM)
		GPIO.output(18, GPIO.LOW)
		GPIO.cleanup()
		response = "light off"

   	except:
      		response = "failed turning light off"

	return jsonify({'response': response})

#host='0.0.0.0'-> so the web server is accessible to any device on the same network, including other computers
#di terminal rasp pi ketik hostname -I , kalo udh dpt IP rasp pi nya, buka di browser pke port 5000
#https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/9
if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
