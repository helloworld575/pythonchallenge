
import re
import urllib2

num = '12345'
num = '8022'
while num is not None:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    pattern = re.compile('and the next nothing is (.*?)$')
    string = response.read()
    #string2 = response.read() the object will be delete after used
    num = re.search(pattern,string).group(1)
    print string
    print string2
    print num
