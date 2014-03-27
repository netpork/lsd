#!/usr/bin/python
from subprocess import *

class Info:

    screen0 = ['---', '---']
    screen1 = ['---', '---']
    screen2 = ['>Restart', '']
    screen3 = ['>Shutdown', '']
    screen4 = ['>Exit', 'Console only!']

    numPages = 5 - 1

    statusCmd = "femon -c 1 | grep FE_HAS_LOCK"
    statusData = None

    def __init__(self):
        pass
    
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
        self.screen0[0] = data[1]
        self.screen0[1] = data[2]
        self.screen1[0] = data[3]
        self.screen1[1] = data[4]

    def noData(self):
        self.screen0[0] = 'signal 0'
        self.screen0[1] = 'snr 0'
        self.screen1[0] = 'ber 00000000'
        self.screen1[1] = 'unc 00000000'

    def runCmd(self, cmd):
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
        output = p.communicate()[0]
        return output
