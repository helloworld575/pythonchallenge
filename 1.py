import urllib2
import re

request = urllib2.Request('http://www.pythonchallenge.com/pc/def/map.html')
response = urllib2.urlopen(request)
pattern = re.compile('<font color="#f000f0">(.*?)</tr>',re.S)
string = re.search(pattern,response.read()).group(1).strip()
sentence = []
for letter in string:
    num = ord(letter)+2
    if num>ord('z'):
        num-=26
    sentence.append(chr(num))
print ''.join(sentence)
hello = 'map'
for letter in hello:
    print chr(ord(letter)+2)
