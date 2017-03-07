import re
import urllib2

request = urllib2.Request('http://www.pythonchallenge.com/pc/def/equality.html')
response = urllib2.urlopen(request)
pattern1 = re.compile('<!--(.*?)-->',re.S)
pattern2 = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',re.S)
strings = re.search(pattern1,response.read()).group(1)
letters = re.findall(pattern2,strings)
letter = []
for word in letters:
    letter.append(word[4])
print ''.join(letter)
