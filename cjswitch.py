#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Author: Alyssa Quek 2014
"""
import os.path
import re
import requests
import json
from sys import argv, version
from csv import reader

URLREGEX = re.compile(
    '^(http(?:s)?\:\/\/[a-zA-Z0-9\-]+(?:\.[a-zA-Z0-9\-]+)*'
    '\.[a-zA-Z]{2,6}(?:\/?|(?:\/[\w\-]+)*)(?:\/?|\/\w+'
    '\.[a-zA-Z]{2,4}(?:\?[\w]+\=[\w\-]+)?)?(?:\&[\w]+\=[\w\-]+)*)$')


def get_data(url):
  """ Get CSV or JSON data given a url

  Args:
    url (str): URL to csv or json data.

  Example:
     get_data('http://blah.co/data.csv')
  """
  try:
    r = requests.get(url, headers={'Connection':'close'})
  except Exception as err:
    print(__file__ + ': Could not get data from ' + url)
    raise err

  if r.status_code >= 300:
    print('[{0}]: Bad request'.format(r.status_code))

  content_type = r.headers['content-type']
  if 'application/json' in content_type:
    return r.json()
  elif 'text/csv' in content_type or 'text/plain' in content_type:
    return [row for row in reader(r.text.splitlines())]
  else:
    print('Unhandled content-type: ' + content_type)
    return

def load_csv(infile):
  """ Load CSV file on disk

  Args:
    infile (str): full file path to csv file

  Example:
    load_csv(os.path.join(os.path.dirname(__file__), 'data.csv'))
  """
  with open(infile, 'rU') as f:
    return [row for row in reader(f)]

def load_json(infile):
  """ Load JSON file on disk

  Args:
    infile (str): full file path to json file

  Example:
    load_json(os.path.join(os.path.dirname(__file__), 'data.json'))
  """
  with open(infile) as json_file:
    return json.load(json_file)

def csv_to_json(csv_input, outfile=None):
  """ Main function to convert CSV from disk or url to JSON file.

  Args:
    csv_input (str): url or full file path to csv
    outfile (str, optional): file path to save JSON data

  Examples:
    csv_to_json('/Documents/data.csv', 'data.json')
    csv_to_json('http://blah.co/data.csv', 'data.json')
  """
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
      if version < '3':
        f.write(unicode(json.dumps(data, ensure_ascii=False)))
      else:
        f.write(json.dumps(data, ensure_ascii=False))
      print('Done. JSON saved in ' + os.path.basename(outfile))
  else:
    return data

if __name__ == '__main__':
  if len(argv) <= 1:
    print('Usage: python cjswitch '
          '<url or path to csv> <optional:outfile path>')
  else:
    csv_to_json(*argv)
