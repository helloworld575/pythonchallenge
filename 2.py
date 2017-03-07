import re
import urllib2

request = urllib2.Request('http://www.pythonchallenge.com/pc/def/ocr.html')
response = urllib2.urlopen(request)
pattern = re.compile('<!--(.*?)-->',re.S)
string = re.findall(pattern,response.read())[1]
word = []
for letter in string:
    if (ord(letter)>=ord('a') and ord(letter)<=ord('z')):
        word.append(letter)
print ''.join(word)
