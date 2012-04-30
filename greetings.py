#!/usr/bin/python

import os, time
from subprocess import call

os.environ['TZ'] = "Australia/Brisbane"

minimumTimeForHuToGreetYou = 10

def greeting(phenny, input):
	# check modification date of file 'lastupdated'
	# if modification date > 4 hours ago, say "good evening" / "good morning" / etc.
	try:
		modificationDate = os.path.getmtime("lastupdated")
	except os.error:
		call(["touch", "lastupdated"])
		return
	if modificationDate < time.time() - minimumTimeForHuToGreetYou:
		localTime = time.localtime()
		if 7 <= localTime.time_hour <= 11:
			phenny.say("Good morning, " + input.nick + ". I trust you slept well.")
		elif 18 <= localTime.time_hour:
			phenny.say("Good evening, " + input.nick + ". I hope you had a good day.")
	call(["touch", "lastupdated"])
	
greeting.rule = r'.*'