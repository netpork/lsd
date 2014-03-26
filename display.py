#!/usr/bin/python

from info import Info
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

class Display:

	lcd = Adafruit_CharLCDPlate()
	info = None
	screen = []
	screenIdx = 0

	def __init__(self):
		self.lcd.clear()
		self.lcd.backlight(self.lcd.ON)
		self.info = Info()

	def show(self):
		if self.screenIdx == 0:
			self.screen = self.info.screen0
		elif self.screenIdx == 1:
			self.screen = self.info.screen1
		elif self.screenIdx == 2:
			self.screen = self.info.screen2
		elif self.screenIdx == 3:
			self.screen = self.info.screen3
		else:
			pass

		s = self.screen[0] + '\n' + self.screen[1]
		self.lcd.clear()
		self.lcd.message(s) 

	def update(self):
		self.lcd.clear()
		self.screenIdx += 1
		if self.screenIdx % 2:
			self.setBackgroundGreen()
		else:
			self.setBackgroundRed()

	def moveUp(self):
		if self.screenIdx == 0:
			self.screenIdx = self.info.numPages
		else:
			self.screenIdx -= 1

	def moveDown(self):
		if self.screenIdx == self.info.numPages:
			self.screenIdx = 0
		else:
			self.screenIdx += 1

	def setBackgroundGreen(self):
		self.lcd.backlight(self.lcd.GREEN)

	def setBackgroundRed(self):
		self.lcd.backlight(self.lcd.RED)

	def setLCDOff(self):
		self.lcd.backlight(self.lcd.OFF)

	def setLCDOn(self):
		self.lcd.backlight(self.lcd.ON)
