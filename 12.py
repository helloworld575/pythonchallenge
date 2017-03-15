content=open("evil2.gfx",'rb').read()
for i in range(5):
    fp = open('12_%d.jpg' %i,'wb')
    fp.write(content[i::5])
    fp.close()