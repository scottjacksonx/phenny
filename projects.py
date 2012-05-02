#!/usr/bin/python

projectList = ["Pedal", "hu"]

def projects(phenny, input):
	if input == "":
		# list the projects
		s = "Which project would you like to open?\n"
		for p in projectList:
			s += +"\t- " + p + "\n"
		phenny.say(s)
	else:
		if input in projectList:
			phenny.say("http://file:///Users/scottjacksonx/git/" + input + "/")
		else:
			phenny.say("You don't have a project called " + input)
			
			
projects.commands = ['project']
projects.priority = 'medium'