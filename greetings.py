#!/usr/bin/python

import os, time
from subprocess import call

os.environ['TZ'] = "Australia/Brisbane"

def greeting(phenny, input):
	# check modification date of file 'lastupdated'
	# if modification date > 4 hours ago, say "good evening" / "good morning" / etc.
	try:
		modificationDate = os.path.getmtime("lastupdated")
	except os.error:
		call(["touch", "lastupdated"])
		return
	if modificationDate < time.gmtime() - 10:
		print time.localtime()
		phenny.say("it's been a while, " + input.nick)
	call(["touch", "lastupdated"])
	
greeting.rule = r'.*'