#!/usr/bin/python

projectList = ["Pedal", "hu"]

projectMap = {
	"Pedal": "/Users/scottjacksonx/Dropbox/Scripts/AppleScript/Projects/Pedal.command"
}

def projects(phenny, input):
	input = input[9:]
	if input == "":
		# list the projects
		s = "Which project would you like to open?\n"
		for p in projectList:
			s = s + "\t- " + p + "\n"
		phenny.say(s)
	else:
		if input in projectList:
			phenny.say("http://file://" + projectMap[input])
		else:
			phenny.say("You don't have a project called " + input)
			
			
projects.commands = ['project']
projects.priority = 'medium'