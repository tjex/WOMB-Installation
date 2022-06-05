#!/usr/bin/python3
# https://www.youtube.com/watch?v=JvQKZXCYMUM

import RPi.GPIO as GPIO
from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=24, trigger=23)

def safe_exit(signum, frame):
	exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

try:
	while True:
		print("Distance: ", sensor.distance * 100)
		sleep(0.1)

except KeyboardInterrupt:
	pass

finally:
	sensor.close()
