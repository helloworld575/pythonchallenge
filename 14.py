from PIL import Image

img = Image.open('wire.png')
handle =Image.new ("RGBA",(100,100), (255, 255, 255))
i=[100,99,99,98]
length = 0
s=0
while(length<=10000):
    for k in range(4):
        length +=i[k]
        for j in range(i[k]):
            handle.putpixel((j,s),img.getpixel((j+length,0)))
        s+=1
        if s==95:
            handle.show()
            break
