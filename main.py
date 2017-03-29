import urllib2
from bs4 import BeautifulSoup as bs
import re

city=raw_input("Please enter the location in this format eg:santa-monica-ca:")
date=raw_input("Please enter the date in this mm/dd/year:")


url = "http://www.accuweather.com/en/us/{0}/10510/month/2146224?monyr={1}".format(city,date)

page = urllib2.urlopen(url)
soup = bs(page, "html.parser")

result = soup.find_all("div",'box')

print result

for res in result:
    print res.tag
    print res.text