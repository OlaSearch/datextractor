# Date extractor for python

### For python 2+ or 3. No external dependencies

## Usage

````
pip install -e git+ssh://git@gitlab.com/olasearch/datextractor.git#egg=datextractor
````

In your python file

````
from datextractor import datetime_parsing

// Outputs an array of tuples
print datetime_parsing('The game is this year')

[('this year', datetime.datetime(2016, 1, 1, 0, 0), (12, 21))]

1. String that was matched `this year`
2. datetime object
3. string position `start` and `end`
````