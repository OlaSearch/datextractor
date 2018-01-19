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
    parser = datetime_parsing(input_text)
    strict_parse = strict_parsing(input_text, parser)
    self.assertEqual(strict_parse[0][4], False)

    input_text = 'The event starts on Monday 12 January 2012'
    parser = datetime_parsing(input_text)
    strict_parse = strict_parsing(input_text, parser)
    self.assertEqual(strict_parse[0][4], True)

    input_text = 'The event starts on Monday 12 January 2012 and is ending tomorrow'
    parser = datetime_parsing(input_text)
    strict_parse = strict_parsing(input_text, parser)
    self.assertEqual(strict_parse[1][4], True)