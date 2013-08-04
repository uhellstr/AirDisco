#!/usr/bin/env python
# coding: Latin-1

####################################################################
#
# AirDisco: Using Piborg's (www.piborg.com) LedBorg
# Revision: 1.0 2013-08-04
#
# by: Ulf Hellström, oraminute@gmail.com
# date: 2013-08-04
#
# This Python program uses the Piborg LedBorg on the Raspberry Pi
# See www.piborg.com for more information on LedBorg
# See http://www.raspberrypi.org for more info on Raspberry Pi
#
# Requires python-daemon to install use
# sudo apt-get install python-daemon
# Requires top to be installed 
# sudo apt-get install top
#
# Code tested on official Raspian-wheezy 
#
#  python AirDisco.py start (to start the daemon)
#  python AirDisco.py stop  (to stop the daemon)
#  python AirDisco.py restart (to restart the daemon)
#
# GNU GENERAL PUBLIC LICENSE
# use this code however you'd like, just keep this license and
# attribute. Let me know if you make hugely, awesome, great changes.
#
####################################################################

######################################################
# Load Library functions we need
#####################################################

import time
import random
import atexit
from subprocess import *
from daemon import runner
  				

####################################################
# Handles extra funtionality whenever the daemon
# is stopped.
####################################################
def exit_handler():
    red = 0
    green = 0
    blue = 0
    color = "%d%d%d" % (red, green, blue)
    LedBorg = open('/dev/ledborg', 'w')
    LedBorg.write(color)
    LedBorg.close()

####################################################
# This is where it is where we do the disco lights
####################################################

class Disco():
    """ Starts the LedBorg pulsing with random colors
        whenever we found that hairtunes process is running.

    """

    def __init__(self):
        random.seed()
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/AirDisco.pid'
        self.pidfile_timeout = 5

    def run_cmd(self, cmd):
        try:
            p = Popen(cmd, shell=True, stdout=PIPE)
            output = p.communicate()[0]
            return output
        except:
            pass

    def checkAirPlay(self):
        cmd = "/usr/bin/top -b -n 1 | head -n 12  | tail -n 5 |awk '/hairtunes/ {print $12}'"
        result = self.run_cmd(cmd)
        if not result:
            return False
        else:
            return True
            
    def run(self):
        while True:
            time.sleep(.5)
            if self.checkAirPlay():
				red = random.randint(0,2)
				green = random.randint(0,2)
				blue = random.randint(0,2)
				color = "%d%d%d" % (red, green, blue)
				LedBorg = open('/dev/ledborg', 'w')
				LedBorg.write(color)
				LedBorg.close()
            else:
				red = 0
				green = 0
				blue = 0
				color = "%d%d%d" % (red, green, blue)
				LedBorg = open('/dev/ledborg', 'w')
				LedBorg.write(color)
				LedBorg.close()
	
####################################################
# main: Init daemon and handle exit
####################################################
if __name__ == "__main__":
    atexit.register(exit_handler)
    app = Disco()
    daemon_runner = runner.DaemonRunner(app)
    daemon_runner.do_action()
