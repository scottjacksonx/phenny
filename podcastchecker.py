import json
import urllib2
from bs4 import BeautifulSoup
import time
import threading

def setup(phenny):
	def checkPodcasts(phenny):
		while True:
			f = open("podcasts.json", "r+")
			podcasts = json.loads(f.read())

			"""
			a podcast looks like this:

			{
				feed_url: "http://something"
				latest_episode_date: "something"
				name: "The Name of the Podcast"
			}
			"""

			for podcast in podcasts:
				print "checking " + podcast["name"]
				xmlSource = urllib2.urlopen(podcast["feed_url"]).read()
				soup = BeautifulSoup(xmlSource)

				latestEpisodePublishedDate = soup.item.pubdate.string
				if latestEpisodePublishedDate != podcast["latest_episode_date"]:
					podcasts[podcasts.index(podcast)]["latest_episode_date"] = latestEpisodePublishedDate
					# say something in chat about it
					phenny.say("New episode of " + podcast["name"] + " available!")
			time.sleep(10)
	targs = (phenny,)
	t = threading.Thread(target=checkPodcasts, args=targs)
	t.start()