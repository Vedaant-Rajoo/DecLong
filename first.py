n,r =map(int,input().split(" "))
l=[]
c1="Bad boi"
c2="Good boi"
for i in range(n):
    o=int(input())
    if o<r:
        l.append(c1)
    else:
        l.append(c2)
for j in l:
    print(j)
