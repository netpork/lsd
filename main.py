#!/usr/bin/python
import sys, subprocess, time
sys.path.append("Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from display import Display 

display = Display()
lcd = display.lcd

lcd.message("shmorni\nshmorni")

#
#
