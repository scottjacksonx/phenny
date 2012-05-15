import json
import urllib2
from bs4 import BeautifulSoup
import time
import threading
import prowlpy

interval = 15 * 60

def setup(phenny):
	def checkPodcasts(phenny):
		channel = open("channel", "r").readline().strip()
		apikey = open("prowl_api_key", "r").readline().strip()
		prowl = prowlpy.Prowl(apikey)
		while True:
			
			# check podcasts
			f = open("podcasts.json", "r")
			podcasts = json.loads(f.read())
			f.close()

			"""
			a podcast looks like this:

			{
				feed_url: "http://something"
				latest_episode_date: "something"
				name: "The Name of the Podcast"
			}
			"""

			for podcast in podcasts:
				try:
					xmlSource = urllib2.urlopen(podcast["feed_url"]).read()
					soup = BeautifulSoup(xmlSource)

					latestEpisodePublishedDate = soup.item.pubdate.string
					if latestEpisodePublishedDate != podcast["latest_episode_date"]:
						print "new episode found"
						podcasts[podcasts.index(podcast)]["latest_episode_date"] = latestEpisodePublishedDate
						phenny.msg(channel, "New episode of " + podcast["name"] + " available!")
						prowl.post(application="hu",event="Podcast",description="New episode of " + podcast["name"] + " available!")
				except:
					print "error getting episodes of " + podcast["feed_url"]
					pass
			f = open("podcasts.json", "w")
			f.write(json.dumps(podcasts))
			f.close()
			
			# check TV shows
			f = open("tv.json", "r")
			shows = json.loads(f.read())
			f.close()

			"""
			a tv show looks like this:

			{
				feed_url: "http://something"
				latest_episode_date: "something"
				name: "The Name of the Show"
			}
			"""

			for show in shows:
				try:
					xmlSource = urllib2.urlopen(show["feed_url"]).read()
					soup = BeautifulSoup(xmlSource)

					latestEpisodePublishedDate = soup.item.pubdate.string
					if latestEpisodePublishedDate != show["latest_episode_date"]:
						print "new episode found"
						shows[shows.index(show)]["latest_episode_date"] = latestEpisodePublishedDate
						phenny.msg(channel, "New episode of " + show["name"] + " available!")
						prowl.post(application="hu",event="TV Show",description="New episode of " + show["name"] + " available!")
				except:
					print "error getting episodes of " + show["feed_url"]
					pass
			f = open("tv.json", "w")
			f.write(json.dumps(shows))
			f.close()
			time.sleep(interval)
	targs = (phenny,)
	t = threading.Thread(target=checkPodcasts, args=targs)
	t.start()