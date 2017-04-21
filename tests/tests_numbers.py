# -*- coding: utf-8 -*-
from unittest import TestCase
from datextractor import number_parsing

"""
  Output of the parser is an array of tuples
  [match, value, (start, end)]
"""

class NumberParsingTestCases(TestCase):
  def test_captured_patterns(self):
    input_text = 'I have 2 kids'
    parser = number_parsing(input_text)
    self.assertIn(2, parser[0])
    self.assertEqual(len(parser), 1)

    input_text = 'I am twenty one years old'
    parser = number_parsing(input_text)
    self.assertIn(21, parser[0])
    self.assertEqual(len(parser), 1)
