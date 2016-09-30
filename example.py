from datextractor import tag, ground
from mx.DateTime import *

tagged_text = tag('The invoice was working on twenty five minutes ago')
print ground(tagged_text, now())