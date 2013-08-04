AirDisco
========

Python Daemon that works with LedBorg and hairtunes (Airplay) on the Raspberry Pi.

To use AirDisco you will need the following:

* A Raspberry Pi with raspian-wheezy and python 2.7.x installed.
* A LedBorg shield from www.piborg.com

You have to make sure the following is installed before running AirDisco.

* LedBorg Libraries (www.piborg.com)
* Shairport Airplay Emulator (http://lifehacker.com/5978594/turn-a-raspberry-pi-into-an-airplay-receiver-for-streaming-music-in-your-living-room)
* python-daemon 
* top

To install necessary libraries and programs except LedBorg and Shairport Airplay Emulator (See above links) do the following:

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python-daemon
sudo apt-get install top

Usage:

	To start using AirDisco that runs in userspace please use the following commands
	
	python AirDisco.py start -- to startup the daemon
	python AirDisco.py stop  -- to stop the daemon
	python AirDisco.py restart -- to restart the daemon
	
Note:

	Test has chowned that the following do not work correctly for terminating the daemon
	chmod +x AirDisco.py
	./AirDisco.py start|stop|restart
	
	So strongly recommend that you use the python AirDisco.py start|stop|restart medthod as described above.
