from scapy.all import *
import sys
import re
'''
Poison - The poisoning part
parseHostNames - open hostnames file, build list.
main - main.
'''
face=0
hostNames=[]
expr=0

def poison():
    if(face):
        print("Interface")
    if(len(hostNames)>0):
        print("HostNames")
    if(expr):
        print("expr")

    print("Poison")

def parseHostNames(filelist):
    try:
        f=open(filelist)
        for line in f:
            x=re.split('\s+',line)
            hostNames.append((x[0],x[1]))
    except:
        print("404 File Not Found!")
        sys.exit(1)

def main():
    arg=0
    while(arg<len(sys.argv)):
        if(sys.argv[arg]=='-i'):
            arg+=1
            face=sys.argv[arg]
        elif(sys.argv[arg]=='-f'):
            print("Checking")
            arg+=1
            parseHostNames(sys.argv[arg])
            print(hostNames)
        else:
            expr=sys.argv[arg]
        arg+=1
    print("Test")

main()
