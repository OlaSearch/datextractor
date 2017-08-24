from datextractor import number_parsing

text = 'Can i hire more than 1 fdw'
text = 'I am twenty-one years old. Can I hire a fdw?'
text = 'Can i hire fdw as 50 years old'
text = 'I have 2 fdws can i hire a 3rd fdw?'
text = 'I earn 2000 dollars, can i hire a maid'
text = 'I earn 10 - 20 dollars, can i hire a maid'
text = 'I earn 10 to 20 dollars, can i hire a maid'

print (str(number_parsing(text)))