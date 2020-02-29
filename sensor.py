from datetime import datetime
import requests
import RPi.GPIO as GPIO
import time
import spidev
import sys

IPADDRESS = ""
channel = 0
spi = spidev.SpiDev()
spi.open(0, 0)

def readadc(channel):
	if ((channel > 7) or (channel < 0)):
		return -1
	r = spi.xfer2([1, 8 << 4, 0])
	data = ((r[1] & 3) << 8) + r[2]
	return data

try:
	while True:
		value = readadc(channel)
		print("Value: " + str(value))

		if value > 0:
			print('CO detected')
			requests.put("http://" + IPADDRESS + ":5000/data/CO",{"CO":"1"})
		else:
			print('No CO detected')
			requests.put("http://" + IPADDRESS + ":5000/data/CO", {"CO":"0"})

		requests.put("http://" + IPADDRESS + ":5000/data/timestamp", {"timestamp":str(datetime.now())})
		time.sleep(1)

except KeyboardInterrupt:
	spi.close()
	sys.exit(0)
