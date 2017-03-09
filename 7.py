from PIL import Image
import urllib2

request = urllib2.Request('http://www.pythonchallenge.com/pc/def/oxygen.png')
response = urllib2.urlopen(request)
fp = file('oxygen.png','wb')
fp.write(response.read())
fp.close()

img = Image.open("oxygen.png")
region = (0,45,610,47)
cropi = img.crop(region)
data = []
for i in range(0,600,7):
    data.append(cropi.getpixel((i,1))[0])
chars = []
for char in data:
    chars.append(chr(char))
print ''.join(chars)
letter = [105,110,116,101,103,114,105,116,121]
word = []
for i in letter:
    word.append(chr(i))
print ''.join(word)