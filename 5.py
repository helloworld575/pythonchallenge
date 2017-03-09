import pickle
import urllib2
import re

html = 'peak.html'
url = 'http://www.pythonchallenge.com/pc/def/'
request = urllib2.Request(url+html)
response = urllib2.urlopen(request)
pattern = re.compile('<peakhell src="(.*?)"/>',re.S)
html = re.search(pattern,response.read()).group(1)
print html
request2 = urllib2.Request(url+html)
response = urllib2.urlopen(request2)
database = pickle.load(response)
for data in database:
    for char in data:
        for i in range(char[1]):
            print char[0],
    print '\n'