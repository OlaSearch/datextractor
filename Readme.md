# Date extractor for python

### For python 2+. Didnt test in python 3. Hard dependency for date manipulation => `egenix-mx-base`

## Usage

````
pip install git@gitlab.com:olasearch/datextractor.git
````

In your python file

````
from datextractor import tag, ground
from mx.DateTime import *

tagged_text = tag('The game is on yesterday')
date_object = today()
print ground(tagged_text, date_object)
````