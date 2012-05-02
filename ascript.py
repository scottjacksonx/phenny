#!/usr/bin/python

def projects(phenny, input):
	input = input[8:]
	phenny.say("http://file:///Users/scottjacksonx/Dropbox/Scripts/AppleScript/" + input + ".command")
			
			
projects.commands = ['script']
projects.priority = 'medium'