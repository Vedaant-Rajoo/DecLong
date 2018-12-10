import sys
import itertools
nodes=int(input())
q=[]
q.append(x)
r=0
vertices=[]
a=0
for i in xrange(0,nodes):
    vertices.append(a)
    a=a+1

def inputgraph():
    cordinates=[]
    cor1=input()

    while cor1!=-1:
        cor2= input("enter y")
        cordinates.append((cor1,cor2))
        cor1= input("enter x or -1 to exit:    ")

    return cordinates

def main():
    cordinates=inputgraph()

if __name__ == '__main__':
    main(