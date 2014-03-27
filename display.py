#!/usr/bin/python

import subprocess
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
        if self.screenIdx == 0: self.screen = self.info.screen0
        elif self.screenIdx == 1: self.screen = self.info.screen1
        elif self.screenIdx == 2: self.screen = self.info.screen2
        elif self.screenIdx == 3: self.screen = self.info.screen3
        elif self.screenIdx == 4: self.screen = self.info.screen4

        s = self.screen[0] + '\n' + self.screen[1]
        self.lcd.clear()
        self.lcd.message(s) 

    def update(self):
        lock = self.info.isLocked()

        # appropriately set backlight
        if lock:
            self.setBackgroundGreen()
            self.info.fillData()
        else:
            self.setBackgroundRed()
            self.info.noData()

        self.show()


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

    def action(self):
        if self.screenIdx == 0: self.action0()
        elif self.screenIdx == 1: self.action1() 
        elif self.screenIdx == 2: self.action2() 
        elif self.screenIdx == 3: self.action3() 
        elif self.screenIdx == 4: self.action4() 

    def action0(self):
        """ action for page 1 """
        pass

    def action1(self):
        """ action for page 2 """
        pass

    def action2(self):
        """ reboot """
        subprocess.call("sync")
        subprocess.call("reboot")
        self.lcd.clear()
        self.lcd.message('Rebooting ...')

    def action3(self):
        """ shutdown """
        subprocess.call("sync")
        subprocess.call(["halt", "-h"])
        self.lcd.clear()
        self.lcd.message('Wait 30 secs\nto unplug...')

    def action4(self):
        self.exit()

    def exit(self):
        self.setLcdOff()
        exit()

    def setBackgroundGreen(self):
        self.lcd.backlight(self.lcd.GREEN)

    def setBackgroundRed(self):
        self.lcd.backlight(self.lcd.RED)

    def setLcdOff(self):
        self.lcd.clear()
        self.lcd.backlight(self.lcd.OFF)

    def setLcdOn(self):
        self.lcd.clear()
        self.lcd.backlight(self.lcd.ON)
