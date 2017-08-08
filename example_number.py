from datextractor import number_parsing

text = 'Can i hire more than 1 fdw'
text = 'I am twenty-one years old. Can I hire a fdw?'
text = 'Can i hire fdw as 50 years old'

print (str(number_parsing(text)))