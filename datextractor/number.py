# -*- coding: utf-8 -*-
import re

hash_units = {
  "zero": 0,
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}

hash_tens = {
  'twenty': 20,
  'thirty': 30,
  'forty': 40,
  'fourty': 40,
  'fifty': 50,
  'sixty': 60,
  'seventy': 70,
  'eighty': 80,
  'ninety': 90
}

hash_scales = {
  "hundred": 100,
  "thousand": 1000,
  "million": 1000000
}

re_units = '|'.join(hash_units.keys())
re_tens = '|'.join(hash_tens.keys())
re_scales = '|'.join(hash_scales.keys())

regex = [
    # Captures scales
    # nine hundred
    (re.compile(
        r'''
        (\b)
        (
          (?P<units>%s)
          (\s)
          (?P<scales>%s)
        )
        (\b)
        '''%(re_units, re_scales),
        (re.VERBOSE | re.IGNORECASE)
        ),
        lambda m: convert_units_scales(m.group('units'), m.group('scales'))
    ),
    # Captures
    # Ninety nine, fourty eight
    (re.compile(
        r'''
        (\b)
        (
          (?P<tens>%s)
          (\s)
          (?P<units>%s)
        )
        (\b)
        '''%(re_tens, re_units),
        (re.VERBOSE | re.IGNORECASE)
        ),
        lambda m: convert_hash_tens(m.group('tens'), m.group('units'))
    ),
    # Captures
    # Ninety
    (re.compile(
        r'''
        (\b)
        (
          (?P<tens>%s)
        )
        (\b)
        '''%(re_tens),
        (re.VERBOSE | re.IGNORECASE)
        ),
        lambda m: convert_hash_tens(m.group('tens'), None)
    ),
    # Captures
    # one, two
    (re.compile(
        r'''
        (\b)
        (
          (?P<units>%s)
        )
        (\b)
        '''%(re_units),
        (re.VERBOSE | re.IGNORECASE)
        ),
        lambda m: convert_hash_tens(None, m.group('units'))
    ),
    # Captures
    # hundred
    (re.compile(
        r'''
        (\b)
        (
          (?P<scales>%s)
        )
        (\b)
        '''%(re_scales),
        (re.VERBOSE | re.IGNORECASE)
        ),
        lambda m: convert_units_scales(None, m.group('scales'))
    ),
    # Captures all digits
    # 45
    (re.compile(
        r'''
        (\b)
        (
          (?P<digits>\d+\.?\d+?)
        )
        (\b)
        ''',
        (re.VERBOSE | re.IGNORECASE)
        ),
        lambda m: float(m.group('digits'))
    ),
]

def convert_hash_tens (tens = None, units = None):
  return (
    hash_tens[tens] if tens is not None else 0
  )  + (
    hash_units[units] if units is not None else 0
  )

def convert_units_scales (units = None, scales = None):
  return (
    hash_units[units] if units is not None else 1
  )  * (
    hash_scales[scales] if scales is not None else 0
  )

# Parses date
def number_parsing (text):
    matches = []
    found_array = []

    # Lowercase text for easy Matching
    text = text.lower()

    # Find the position in the string
    for r, fn in regex:
        for m in r.finditer(text):
            matches.append((m.group(), fn(m), m.span()))

    # print (matches)

    # Wrap the matched text with TAG element to prevent nested selections
    for match, value, spans in matches:
        subn = re.subn('(?!<NUMBER_TAG[^>]*?>)' + match + '(?![^<]*?</NUMBER_TAG>)', '<NUMBER_TAG>' + match + '</NUMBER_TAG>', text)
        text = subn[0]
        isSubstituted = subn[1]
        if isSubstituted != 0:
            found_array.append((match, value, spans))

    # To preserve order of the match, sort based on the start position
    return sorted(found_array, key = lambda match: match and match[2][0])
