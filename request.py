#!/usr/bin/env python3
""" A module to request the apimfor the number facts"""

import requests

def number_api(num):
	"""A function to request the fun fact about the number"""

	#define the url to query
	url = f"http://numbersapi.com/{num}/math"
	res = requests.get(url)

	return res.text