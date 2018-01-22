from datextractor import datetime_parsing, strict_datetime_parsing, number_parsing

# text = '<p>First quarter of 2016 and tomorrow and next 2 years</p>'
# text = '<p>10th of Feb 2017</p>'
# text = '<p>twentyth March twenty 18</p>'
# text = '<p>jan 2018</p>'
text = '<p>27 August 17</p>'#, 25 october in the day of Monday 12 January 2012</p>'
text = 'next month'
text = '25/03/1980'
text = 'my helper is born on july 23 1994, can i hire her'
text = 'i was born since 2000'
text = 'gdp between 2004 and 2010'
# text = 'my helper just got medication check in 23-05-2017, now need medication check again'
# text = 'my helper just got medication check in 23/05/2017, now need medication check again'
# text = 'last months'
# text = 'next 2 year'
# text = 'this week'
# text = 'today'
text = '2012-2013'
text = 'this december at 2pm'
text = '2 weeks ago'
text = '12 november'
text = 'yesterday'
text = 'The event starts on Monday 12 January 2012 and is ending may be tomorrow'
# text = 'Monday 12 Jan 2012 12:23pm'
# text = '<p>twenty first april twenty seventeen</p>'
# text = '<p>21st april twenty seventeen</p>'
# text = '<p>21st of april 20 nineteen</p>'
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

print (strict_datetime_parsing(text))
print (number_parsing('2'))