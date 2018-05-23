import __future__
import os, sys, json
from urllib import quote_plus as quote_plus
from urllib2 import urlopen as urlopen
import json
import csv
import pandas as pd

mapbox_access_token = 'pk.eyJ1Ijoic2VsaW5hd2oiLCJhIjoiY2pnZ3Z0cDU3MDJqdDJxbjQzbWRzMW1ndyJ9.nanlbnuzscLPUZ56WU3gvA'

def geocode(query):
    # mapbox_access_token = 'pk.eyJ1Ijoic2VsaW5hd2oiLCJhIjoiY2pnZ3Z0cDU3MDJqdDJxbjQzbWRzMW1ndyJ9.nanlbnuzscLPUZ56WU3gvA'
    """
    Submit a geocoding query to Mapbox's geocoder.
    Args:
        mapbox_access_token (str): valid Mapbox access token with geocoding permissions
        query (str): input text to geocode
    """
    resp = urlopen('https://api.tiles.mapbox.com/geocoding/v5/mapbox.places/{query}.json?access_token={token}'.format(query=quote_plus(query), token=mapbox_access_token))
    data = json.loads(resp.read().decode('utf-8'))
    print data['features'][0]['context'][0]['text']

df = pd.read_csv('rats_coords.csv')
lat = df.ix[:,0]
lon = df.ix[:,1]
for i in range(0, len(df)):
    coords = str(lat[i]) + ", " + str(lon[i])
    geocode(coords)
