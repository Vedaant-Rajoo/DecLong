import random
l=[0,1,2,3,4,5,6,7,8,9,10]
while len(l)>2:
    r=random.randint(l[0],l[-1])
    print ('1 ',r)
    m=int(input())
    if m==1:
        del l[(l[r+1]):]
        print (l)
    else:
        del l[0:(l[r+1])]
        print (l)