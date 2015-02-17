#!/usr/bin/python

from bs4 import BeautifulSoup
from PIL import Image
# import Image
import requests
import urllib
import cStringIO
import csv

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

		x11_grays = ["(0, 0, 0)","(3, 3, 3)","(5, 5, 5)","(8, 8, 8)","(10, 10, 10)","(13, 13, 13)","(15, 15, 15)","(18, 18, 18)","(20, 20, 20)","(23, 23, 23)","(26, 26, 26)","(28, 28, 28)","(31, 31, 31)","(33, 33, 33)","(36, 36, 36)","(38, 38, 38)","(41, 41, 41)","(43, 43, 43)","(46, 46, 46)","(48, 48, 48)","(51, 51, 51)","(54, 54, 54)","(56, 56, 56)","(59, 59, 59)","(61, 61, 61)","(64, 64, 64)","(66, 66, 66)","(69, 69, 69)","(71, 71, 71)","(74, 74, 74)","(77, 77, 77)","(79, 79, 79)","(82, 82, 82)","(84, 84, 84)","(87, 87, 87)","(89, 89, 89)","(92, 92, 92)","(94, 94, 94)","(97, 97, 97)","(99, 99, 99)","(102, 102, 102)","(105, 105, 105)","(107, 107, 107)","(110, 110, 110)","(112, 112, 112)","(115, 115, 115)","(117, 117, 117)","(120, 120, 120)","(122, 122, 122)","(125, 125, 125)","(127, 127, 127)","(130, 130, 130)","(133, 133, 133)","(135, 135, 135)","(138, 138, 138)","(140, 140, 140)","(143, 143, 143)","(145, 145, 145)","(148, 148, 148)","(150, 150, 150)","(153, 153, 153)","(156, 156, 156)","(158, 158, 158)","(161, 161, 161)","(163, 163, 163)","(166, 166, 166)","(168, 168, 168)","(171, 171, 171)","(173, 173, 173)","(176, 176, 176)","(179, 179, 179)","(181, 181, 181)","(184, 184, 184)","(186, 186, 186)","(189, 189, 189)","(191, 191, 191)","(194, 194, 194)","(196, 196, 196)","(199, 199, 199)","(201, 201, 201)","(204, 204, 204)","(207, 207, 207)","(209, 209, 209)","(212, 212, 212)","(214, 214, 214)","(217, 217, 217)","(219, 219, 219)","(222, 222, 222)","(224, 224, 224)","(227, 227, 227)","(229, 229, 229)","(232, 232, 232)","(235, 235, 235)","(237, 237, 237)","(240, 240, 240)","(242, 242, 242)","(245, 245, 245)","(247, 247, 247)","(250, 250, 250)","(252, 252, 252)","(255, 255, 255)"]

		'''
		f = open("grays.csv")
		csv_f = csv.reader(f, delimiter = "\t")

		for row in csv_f:
			x11_grays.append(str(row[0]))
		'''

		for color in data:
			color_string = str(color)
			if color_string in x11_grays:
				grays.append(color_string)

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
