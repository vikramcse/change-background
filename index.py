import urllib2
import urllib
import json
import ctypes
import getpass
import os
import sys
import time

current_user = getpass.getuser()
default_image_dir = "/home/"+ current_user +"/Pictures/download.jpg"
if len(sys.argv) >= 2:
	auto_set_in_24_hrs = sys.argv[1]
else:
	auto_set_in_24_hrs = 'default'

def parse_bing_for_url():
	data = json.load(urllib2.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-IN'))
	image_url = 'http://' + 'www.bing.com' + data['images'][0]['url']
	return image_url

def set_background_for_linux():
	image = urllib.urlretrieve(parse_bing_for_url(), default_image_dir)
	print "Image downloaded..."
	os.system ("gsettings set org.gnome.desktop.background picture-uri file://" + default_image_dir)

if auto_set_in_24_hrs == 'auto':	
	while True:
		set_background_for_linux()
		print "Running in background in auto refresh mode ctrl-c for exit."
		print "Next background will set in 24 hrs"
		#change background every 12 hrs
		time.sleep(43200)
elif auto_set_in_24_hrs == 'default':
	set_background_for_linux()