from scapy.all import *
import sys
import time
from scapy.layers.http import HTTPRequest
'''
Default to wlp3s0 
'''
def requests(pkt):
    op="TLS"
    src=pkts[i].getlayer(IP).src + ":" +str(pkts[i].getlayer(TCP).sport)
    dst=pkts[i].getlayer(IP).dst+ ":" +str(pkts[i].getlayer(TCP).dport)
    tim=str(time.asctime(time.localtime(x)))

    #Additional info for HTTP Requests, not TLS
    if pkt.haslayer(HTTPRequest):
        op="HTTP"
        host = pkt[HTTPRequest].Host.decode()
        met=pkt[HTTPRequest].Method.decode()
        path = pkt[HTTPRequest].Path.decode()

        #Capture Post Data - This can mean Login Credentials!!!
        if met=="POST":
            if pkt.haslayer(scapy.all.Raw):
                cred=(str(pkt[scapy.all.Raw]))
                cred=cred.replace('b','',1)
                cred=cred,replace('\'','')

face="wlp3s0"
x=0
while(x<len(sys.argv)):
    if(sys.argv[x]=='-i'):
        face=sys.argv[x+1]
    x+=1

pkts= sniff(filter='tcp',iface=face,prn=requests)
'''
for i in range(3):
    #print(pkts[i].summary())
    src=pkts[i].getlayer(IP).src + ":" +str(pkts[i].getlayer(TCP).sport)
    dst=pkts[i].getlayer(IP).dst+ ":" +str(pkts[i].getlayer(TCP).dport)
    tim=str(time.asctime(time.localtime(x)))
    print(tim+ " "+ src + "->" + dst)
    print("\n\n\n\n\n")
    #print(pkts[i].getlayer(IP).dst)
    x=(pkts[i].getlayer(TCP).time)
'''
