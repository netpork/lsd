#!/usr/bin/python
# pylint: disable-msg=C0103
import sys, time
sys.path.append("Adafruit-Raspberry-Pi-Python-Code/Adafruit_CharLCDPlate")
# from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from display import Display 

display = Display()
lcd = display.lcd
prevButton = -1
lastTime = time.time()
REFRESH_TIME = 3.0

display.show()


while True:
    button = lcd.buttons()
    if button is not prevButton:
        if lcd.buttonPressed(lcd.UP):
            display.moveUp()
            display.show()
        elif lcd.buttonPressed(lcd.DOWN):
            display.moveDown()
            display.show()
        elif lcd.buttonPressed(lcd.SELECT):
            display.action()

        prevButton = button
        lastTime = time.time()
    else:
        now = time.time()
        since = now - lastTime

        if since > REFRESH_TIME or since < 0.0:
            # display.update()
            lastTime = now
