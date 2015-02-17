#!/usr/bin/python

from bs4 import BeautifulSoup
from PIL import Image
# import Image
import requests
import urllib
import cStringIO

class ShadesOfGray:

	def __init__(self, username):
		self.data = self.get_grays(username)

	def get_grays(self, username):
		r = requests.get("http://twitter.com/" + username)

		soup = BeautifulSoup(r.text)

		page_title = soup.find("title").text

		avatar_url = soup.find("img", attrs = { "class": "ProfileAvatar-image" })["src"]

		all_colors = self.get_colors(avatar_url)

		return self.count_grays(all_colors)

	def count_grays(self, data):
		grays = []

		for color in data:
			if color[0] == color[1] == color[2]:
				grays.append(color)

		return {
			"all_grays": grays,
			"num_grays": len(grays),
			"all_colors": data,
			"num_colors": len(data)
		}

	def get_colors(self, url):

		self.url = url

		image_file = cStringIO.StringIO(urllib.urlopen(url).read())

		image_object = Image.open(image_file)

		colors = {}

		for color in image_object.getdata():
			colors[color] = colors.get(color, 0) + 1

		return colors