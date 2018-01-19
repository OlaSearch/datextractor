# -*- coding: utf-8 -*-
from unittest import TestCase
from datetime import timedelta, date, datetime
from datextractor import datetime_parsing, strict_parsing

"""
  Output of the parser is an array of tuples
  [match, value, (start, end)]
"""

class DateTimeParsingTestCases(TestCase):
  def test_captured_patterns(self):
    base_date = datetime.now()

    input_text = 'The event is on Monday 12 January 2012'
    parser = strict_parsing(input_text)
    self.assertEqual(parser[0][4], False)

    input_text = 'The event starts on Monday 12 January 2012'
    parser = strict_parsing(input_text)
    self.assertEqual(parser[0][4], True)

    input_text = 'The event starts on Monday 12 January 2012 and is ending tomorrow'
    parser = strict_parsing(input_text)
    self.assertEqual(parser[1][4], True)