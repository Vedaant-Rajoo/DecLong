import random
n,c=map(int,input().split())
l=list(range(1,n+1))
while len(l)>2:
    r=random.randint(l[0],l[-1])
    print("1 ",r)
    m=int(input())
    if m==1:
        del l[(l[r]):]
        print (l)
    elif m==0:
        del l[0:(l[r+1])]
        print (l)
print ('1 ',l[0])
a=int(input())
if a==0:
    print('3 ',l[1])
else:
    print('galat hai!!!!!')




