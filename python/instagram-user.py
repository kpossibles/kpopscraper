import csv
import requests
from bs4 import BeautifulSoup
import re
import json
import codecs
from datetime import datetime, timezone
from urllib.parse import urlparse
import sys
import ctypes
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

datafile = 'z-artist-names.csv'
userdata = list(csv.reader(open(datafile,encoding='utf-8')))
usernames = []
for row in userdata:
    if row[3]!='' and row[3]!='Instagram':
        usernames.append((urlparse(row[3]).path).split('/')[1])
# usernames = ['nuestaron','optimushwang','realbaekho', 'pockyjr', 'glorypath']
posts = []
def clearline(msg):
	CURSOR_UP_ONE = '\033[K'
	ERASE_LINE = '\x1b[2K'
	sys.stdout.write(CURSOR_UP_ONE)
	sys.stdout.write(ERASE_LINE+'\r')
	print(msg, end='\r')

# proxies = {'http':'http://10.10.0.0:0000', 'https': 'http://120.10.0.0:0000'}
for name in usernames:
	url = 'https://www.instagram.com/'+name
	# print(url)
	try:
		r = requests.get(url, timeout=5)
		if r.status_code == 200 and r.status_code != 404:
			soup = BeautifulSoup(r.content, 'html.parser')
			scripts = soup.find_all('script', type="text/javascript",
								text=re.compile('window._sharedData'))
			stringified_json = scripts[0].get_text().replace(
				'window._sharedData = ', '')[:-1]
			stringified_json = codecs.encode(stringified_json, encoding='utf-8')
			out = json.loads(stringified_json)['entry_data']['ProfilePage'][0]
			user = out["graphql"].get("user")

			profilepic = user.get("profile_pic_url")
			# print(profilepic)
			edges = user["edge_owner_to_timeline_media"]["edges"]

			for x in edges:
				ts = int(x["node"]["taken_at_timestamp"])
				caption = x["node"]["edge_media_to_caption"]["edges"]
				if(len(caption) != 0):
					caption = caption[0]["node"]["text"]
				# print("url", "http://instagram.com/p/"+x["node"]["shortcode"])
				# print("thumbnail",x["node"]["thumbnail_src"])
				# print("caption",caption)
				# print("likes", x["node"]["edge_liked_by"]['count'])
				# print("comments", x['node']['edge_media_to_comment']['count'])
				# print()

				# utc_time = datetime.utcfromtimestamp(ts)
				# local_time = utc_time.astimezone()
				# local_time.strftime("%x %X (%Z)")
				tmp = {"url": "http://instagram.com/p/"+x["node"]["shortcode"],
								"thumbnail": x["node"]["thumbnail_src"],
								"username": name,
								"profile_pic": profilepic,
								"caption": caption,
								"likes": x["node"]["edge_liked_by"]['count'],
								"comments": x['node']['edge_media_to_comment']['count'],
								"timestamp": ts
				}
				posts.append(tmp)
			# print('Scraping DONE:', name)
			clearline('Scraping DONE: '+name)
			json_file = open('kpop-ig-posts.json', 'w')
			json.dump(posts, json_file)
			json_file.close()
		else:
			err = "%s ERROR: %d" % (name,r.status_code)
			clearline (err)
	except requests.Timeout as e:
		print("It is time to timeout", str(e))

# json_file = open('kpop-ig-posts.json', 'w')
# json.dump(posts, json_file)
# json_file.close()

print('completed kpop instagram scraping')

