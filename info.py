#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
from subprocess import *

class Info:
    screen0 = ['    Shmarni     ', '     v0.42      ']
    screen1 = ['---', '---']
    screen2 = ['---', '---']
    screen3 = ['>Reboot', '']
    screen4 = ['>Shutdown', '']
    screen5 = ['>Exit', 'Console only!']

    numPages = 6 - 1

    statusCmd = "femon -c 1 | grep FE_HAS_LOCK"
    dsmccCMd = "tail -n 2 /home/pi/tvweb/log/`date +%F`.log"
    statusData = None
    dsmccData = None

    signalTotal = 65535 - 22000
    signalBase = 22000

    def __init__(self):
        self.getStatus()
    
    def isLocked(self):
        self.getStatus()
   
        if self.statusData.find('FE_HAS_LOCK') != -1:
            return True
        else:
            return False

    def getStatus(self):
        self.statusData = self.runCmd(self.statusCmd)

    def fillData(self):
        data = self.statusData.split(' | ')
        signal = self.calculateSignal(data[1][-4:])
        status = self.dsmccInfo().split('\n')

        self.screen0[0] = 'signal ' + signal + '%'
        self.screen0[1] = data[2]
        self.screen1[0] = data[3]
        self.screen1[1] = data[4]
        self.screen2[0] = status[0][:16]
        self.screen2[1] = status[1][:16]

    def noData(self):
        self.screen0[0] = 'signal 0%'
        self.screen0[1] = 'snr 0'
        self.screen1[0] = 'ber 00000000'
        self.screen1[1] = 'unc 00000000'
        self.screen2[0] = '---'
        self.screen2[1] = '---'

    def calculateSignal(self, signalHex):
        decimalGiven = int(signalHex, 16) - self.signalBase
        if decimalGiven < 0:
            return '0'
        signal = (float(decimalGiven) / float(self.signalTotal)) * 100
        return str(int(math.ceil(signal)))

    def dsmccInfo(self):
        self.dsmccData = self.runCmd(self.dsmccCMd)
        return self.dsmccData

    def runCmd(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
        output = p.communicate()[0]
        return output
