from datetime import datetime
import requests
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
GPIO.setup(27, GPIO.OUT)

try:
	while True:
		input = GPIO.input(18)
		print(input)
		if input:
			print('CO detected')
			requests.put("http://140.141.208.99:5000/data/CO",{"CP":"1"})
		else:
			print('No CO detected')
			requests.put("http://140.141.208.99:5000/data/CO", {"CO":"0"})

		requests.put("http://140.141.208.99:5000/data/timestamp", {"timestamp":str(datetime.now())})
		time.sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
