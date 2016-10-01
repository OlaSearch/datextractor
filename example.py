from datextractor import tag, ground, tag_phone, tag_email, tag_url
from mx.DateTime import now

# tagged_text = tag('The invoice was working on twenty five minutes ago.')
tagged_text = tag('The event is 25 minutes from now. The invoice was working on 10 days later. Hello my email address is rmdort@gmail.com and hello@hotmail.com. Hello my phone number is +9190291420. The current year is 2010')
# tagged_text = tag('The invoice was working on 10 days later.')
print ground(tag_url(tag_email(tag_phone(tagged_text))), now())
# print tag_phone('Hello my phone number is +91 90291420')
# print tag_email('Hello my email address is rmdort@gmail.com and hello@hotmail.c')
# print tag_url('Hello my website url is http://www.olasearch.com')