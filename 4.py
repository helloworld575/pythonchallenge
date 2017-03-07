import re
import urllib2

num = '12345'
num = '8022'
while num is not None:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    pattern = re.compile('and the next nothing is (.*?)$')
    num = re.search(pattern,response.read()).group(1)
    print response.read()
    print num