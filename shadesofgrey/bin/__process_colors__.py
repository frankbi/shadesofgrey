def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

import csv

with open("x11grays.csv") as f:
		f_reader = csv.reader(f)
		for row in f_reader:
			print hex_to_rgb(row[1])