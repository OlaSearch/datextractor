from datextractor import datetime_parsing, tag_phone, tag_email, tag_url

# tagged_text = tag('The invoice was working on twenty five minutes ago.')
tagged_text = datetime_parsing('The event is 25 min from now. The invoice was working on 10 days later. Hello my email address is rmdort@gmail.com and hello@hotmail.com. Hello my phone number is +9190291420. The current year is 2010. Day before tomorrow')
# tagged_text = tag('The invoice was working on 10 days later.')
print tagged_text
# print tag_phone('Hello my phone number is +91 90291420')
# print tag_email('Hello my email address is rmdort@gmail.com and hello@hotmail.c')
# print tag_url('Hello my website url is http://www.olasearch.com')