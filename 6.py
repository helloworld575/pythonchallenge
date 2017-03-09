import re
import zipfile
pattern = re.compile('Next nothing is (.*?)$',re.S)
num = '90052'
data = []
sum = 0
try:
    while(1):
        data.append(num+'.txt')
        name = 'channel/'+num+'.txt'
        fp = open(name,'r')
        string = fp.readline()
        print string
        num = re.search(pattern,string).group(1)
        print num
except:
    print name

z = zipfile.ZipFile('channel.zip')
for i in data:
    c = z.getinfo(i).comment.decode()
    print c,
