#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import re
import sys
import os
import cjswitch

class CjSwitchTest(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.infile = 'fantasy.csv'
    self.inurl = 'https://raw.github.com/alyssaq/cjswitch/master/fantasy.csv'
    self.outfile = 'fantasy.json'
    self.expected_result = [['id', 'type', 'color'],
                            ['1', 'magical', 'rainbow'],
                            ['2', 'plain', 'white'],
                            ['3', 'darkness', 'black'],
                            ['4', 'mystical', 'sapphire blue']]
  @classmethod
  def tearDownClass(self):
    if os.path.isfile(self.outfile):
      os.remove(self.outfile)

  def verify_result(self, result):
    self.assertEqual(len(result), len(self.expected_result))
    self.assertEqual(result, self.expected_result)

  def test_CSVurl_to_JSON(self):
    res = cjswitch.csv_to_json(self.inurl)
    self.verify_result(res)

  def test_CSVfile_to_JSON(self):
    res = cjswitch.csv_to_json(self.infile)
    self.verify_result(res)

  def test_CSVurl_to_JSONfile(self):
    cjswitch.csv_to_json(self.inurl, self.outfile)
    self.assertTrue(os.path.isfile(self.outfile))
    res = cjswitch.load_json(self.outfile)
    self.verify_result(res)

  def test_CSVfile_to_JSONfile(self):
    cjswitch.csv_to_json(self.inurl, self.outfile)
    self.assertTrue(os.path.isfile(self.outfile))
    res = cjswitch.load_json(self.outfile)
    self.verify_result(res)

if __name__ == '__main__':
    unittest.main()