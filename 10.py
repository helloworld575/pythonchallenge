a = ['1','11']

def nex(b):
    num = []
    i=0
    while(i<len(b)):
        j = 0
        c = b[i]
        while i<len(b) and c==b[i]:
            j+=1
            i+=1
        i-=1
        num.append(str(j))
        num.append(c)
        i+=1
    return ''.join(num)


for i in range(1,30):
    b = a[i]
    c = nex(b)
    a.append(c)
print a
print len(a[30])