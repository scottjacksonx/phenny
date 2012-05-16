import json
import urllib
from bs4 import BeautifulSoup
import time
import threading
import sqlite3

interval = 3 * 60

def setup(phenny):
	def checkCycles(phenny):
		url = "http://api.citybik.es/citycycle.json"
		stationsString = str(urllib.urlopen(url).read())
		
		atts = ["id", "name", "lat", "lng", "bikes", "free", "timestamp"]
		for att in atts:
			logging.info("replacing: " + att)
			stationsString = stationsString.replace(att+":", "\"" + att + "\":")
			
		stations = json.loads(stationsString)
			
		"""
		Table cycles:
		
		int timestamp
		text json
		"""
		
		conn = sqlite3.connect("citycycle.db")
		c = conn.cursor()
		c.execute("insert into cycles VALUES (?,?", (int(time.time()), json.dumps(stations)))
		conn.commit()
		c.close()
		time.sleep(interval)
	targs = (phenny,)
	t = threading.Thread(target=checkCycles, args=targs)
	t.start()