from datextractor import datetime_parsing, tag_phone, tag_email, tag_url

text = '<p>The invoice was working on twenty five minutes ago. And today. Monday 12 January 2012. I am going another monday. And 12 days before</p>'
# text = '<p>The invoice was working on twenty five minutes ago.</p>'
# print datetime_parsing(text)
# tagged_text = datetime_parsing('The event is 25 min from now. The invoice was working on 10 days later. Hello my email address is rmdort@gmail.com and hello@hotmail.com. Hello my phone number is +9190291420. The current year is 2010. Day before tomorrow')
# tagged_text = tag('The invoice was working on 10 days later.')
# print tagged_text
# print tag_phone('Hello my phone number is +91 90291420')
# print tag_email('Hello my email address is rmdort@gmail.com and hello@hotmail.c')
# print tag_url('Hello my website url is http://www.olasearch.com')

print datetime_parsing(text)