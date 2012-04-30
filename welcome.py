#!/usr/bin/python

def welcome(phenny, input):
	phenny.say("Welcome back, " + input.nick)
	
welcome.event = 'JOIN'
welcome.rule = r'.*'