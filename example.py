from datextractor import tag, ground
from mx.DateTime import *

# tagged_text = tag('The invoice was working on twenty five minutes ago.')
tagged_text = tag('The invoice was working on 10 days later.')
print ground(tagged_text, now())