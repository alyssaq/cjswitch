#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from json import dumps
from csv import reader
import os.path
import re
from sys import argv

URLREGEX = re.compile('^(http(?:s)?\:\/\/[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*\.[a-zA-Z]{2,6}(?:\/?|(?:\/[\w\-]+)*)(?:\/?|\/\w+\.[a-zA-Z]{2,4}(?:\?[\w]+\=[\w\-]+)?)?(?:\&[\w]+\=[\w\-]+)*)$')

""" 
Get CSV or JSON data given a url

Parameters
----------
url: URL to csv or json data. 

Example: get_data('http://blah.co/data.csv')
"""
def get_data(url):
  try:
    r = requests.get(url)
  except Exception as err:
    print(__file__ + ': Could not get data from ' + url)
    raise err

  if r.status_code >= 300:
    print '[{0}]: Bad request'.format(r.status_code)

  content_type = r.headers['content-type']
  if 'application/json' in content_type:
    return r.json()
  elif 'text/csv' in content_type or 'text/plain' in content_type:
    return [row for row in reader(r.content.splitlines())]
  else:
    print('Unhandled content-type: ' + content_type)
    return

""" 
Load CSV file on disk

Parameters
----------
infile: full file path to csv file

Example: load_csv(os.path.join(os.path.dirname(__file__), 'data.csv'))
"""
def load_csv(infile):
  with open(infile, 'rU') as f:
    return [row for row in reader(f)]

""" 
Main function to convert CSV from disk or url to JSON file.

Parameters
----------
csv_input: url or full file path to csv
outfile: file path to save JSON data

Examples: 
  csv_to_json('/Documents/data.csv', 'data.json')
  csv_to_json('http://blah.co/data.csv', 'data.json')
"""

def csv_to_json(csv_input, outfile=None):
  if URLREGEX.match(csv_input):
    data = get_data(csv_input)
  elif os.path.isfile(csv_input):
    data = load_csv(csv_input)
  else:
    print('Invalid URL or non-existent csv file: ' + csv_input)
    return

  if outfile is not None:
    from io import open
    with open(outfile, 'w', encoding='utf-8') as f:
      f.write(unicode(dumps(data, ensure_ascii=False)))
      print('Done. JSON saved in ' + os.path.basename(outfile))
  else:
    return data

if __name__ == '__main__':
  if len(argv) <= 1:
    print("Usage: python cjswitch <url or path to csv> <optional:outfile path>")
    exit()

  if len(argv) == 2:
    csv_to_json(argv[1])
  else:
    csv_to_json(argv[1], argv[2])