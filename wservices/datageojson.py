# datageojson.py
# Autograder: Using the GeoJSON API on https://www.py4e.com/lessons/servces

from urllib.request import urlopen
from urllib.parse import urlencode
import json


svcurl = 'http://py4e-data.dr-chuck.net/json?'

loc = input("Enter location: ")
# if len(loc) < 1: loc = 'South Federal University'
if len(loc) < 1: loc = "Fachhochschule FH Salzburg"

prms = dict()
prms['address'] = loc
prms['key'] = 42

url = svcurl + urlencode(prms)
print("Retrieving", url)
data = urlopen(url).read() # bytes
print("Retrieved", len(data))
js = json.loads(data) # dict
place_id = js["results"][0]["place_id"]
print("Place id", place_id)