from scapy.all import *
import sys
import time
from scapy.layers.http import HTTPRequest
from scapy.layers.tls import *
import cryptography
'''
Default to wlp3s0 
'''
def requests(pkt):
    op=""
    #Additional info for HTTP Requests, not TLS
    if pkt.haslayer(HTTPRequest):
        src=pkt.getlayer(IP).src + ":" +str(pkt.getlayer(TCP).sport)
        dst=pkt.getlayer(IP).dst+ ":" +str(pkt.getlayer(TCP).dport)
        x=(pkt.getlayer(TCP).time)
        tim=str(time.asctime(time.localtime(x)))
        op="HTTP"
        host = pkt[HTTPRequest].Host.decode()
        met=pkt[HTTPRequest].Method.decode()
        path = pkt[HTTPRequest].Path.decode()
        #Capture Post Data - This can mean Login Credentials!!!        
        if met=="POST":
            if pkt.haslayer(scapy.all.Raw):
                cred=(str(pkt[scapy.all.Raw]))
                cred=cred.replace('b','',1)
                cred=cred.replace('\'','')
        print(tim+ " " +op+" "+src +" -> " + dst +" " + host + " " +met + " "+ path)

    elif pkt.haslayer('TLS'):
        print("WE MADE IT")



def tst(pkt):
    pkt.show()
    print("LALALALALLALA")

face="wlp3s0"
x=0
while(x<len(sys.argv)):
    if(sys.argv[x]=='-i'):
        face=sys.argv[x+1]
    x+=1
load_layer("http")
load_layer("tls")
#filter='tcp'
pkts= sniff(iface=face,prn=requests)