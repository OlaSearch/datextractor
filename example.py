from datextractor import datetime_parsing

# text = '<p>First quarter of 2016 and tomorrow and next 2 years</p>'
# text = '<p>10th of Feb 2017</p>'
# text = '<p>twentyth March twenty 18</p>'
text = '<p>jan 2018</p>'
# text = '<p>The event is on Monday 12 January 2012</p>'
# Todo : last 2 months. range
# text = '<p>The invoice was working on twenty five minutes ago.</p>'
# print datetime_parsing(text)
# text = 'The event is 25 min from now. The invoice was working on 10 days later. Hello my email address is rmdort@gmail.com and hello@hotmail.com. Hello my phone number is +9190291420. The current year is 2010. Day before tomorrow'
# tagged_text = tag('The invoice was working on 10 days later.')
# print tagged_text
# print tag_phone('Hello my phone number is +91 90291420')
# print tag_email('Hello my email address is rmdort@gmail.com and hello@hotmail.c')
# print tag_url('Hello my website url is http://www.olasearch.com')

print (datetime_parsing(text))