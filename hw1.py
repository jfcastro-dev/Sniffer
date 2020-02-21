from scapy.all import *
import sys
import time
from scapy.layers.http import HTTPRequest
from scapy.layers.tls import *
import cryptography

def requests(pkt):
    op=""
    if pkt.haslayer(HTTPRequest):
        src=pkt.getlayer(IP).src + ":" +str(pkt.getlayer(TCP).sport)
        dst=pkt.getlayer(IP).dst+ ":" +str(pkt.getlayer(TCP).dport)
        x=(pkt.getlayer(TCP).time)
        tim=str(time.asctime(time.localtime(x)))
        op="HTTP"
        host = pkt.getlayer(HTTPRequest).Host.decode()
        met=pkt.getlayer(HTTPRequest).Method.decode()
        path = pkt.getlayer(HTTPRequest).Path.decode()
        '''
        This is commented out because it is outside the scope of the HW.
        It captures data from post requests.Whilst this is more 
        or less useless as is, if you combined this with
        SSL stripping, you'd basically have access to confidential data.
        Also jail time.
        if met=="POST":
            if pkt.haslayer(scapy.all.Raw):
                cred=(str(pkt[scapy.all.Raw]))
                cred=cred.replace('b','',1)
                cred=cred.replace('\'','')
        '''
        print(tim+ " " +op+" "+src +" -> " + dst +" " + host + " " +met + " "+ path)

    elif pkt.haslayer('TLS Handshake - Client Hello'):
        src=pkt.getlayer(IP).src + ":" +str(pkt.getlayer(TCP).sport)
        dst=pkt.getlayer(IP).dst+ ":" +str(pkt.getlayer(TCP).dport)
        x=(pkt.getlayer(TCP).time)
        tim=str(time.asctime(time.localtime(x)))
        op=pkt.getlayer('TLS Extension - Supported Versions (for ClientHello)').versions
        maxvers=769 #some weird edge cases don't return anything so we'll assume default to 1.0
        for i in op:
            if(i>maxvers):
                maxvers=i
        #This is a bit of a hack - number returned is SSL Code. 769 = TLS 1.0,770=1.1, 771=1.2, etc
        op=(float(maxvers)-769.0)*0.1+1.0
        op="TLS v" + str(op)
        host= str(pkt.getlayer('TLS Extension - Server Name').servernames[0])[14:].replace('\'',"")
        print(tim+ " " + op + " " + src +" ->  " +dst +" "+host)

def tst(pkt):
    if (pkt.haslayer('TLS Extension - Server Name')):
        pkt.show()

face=False
tbf=False
prevdump=False
x=0
while(x<len(sys.argv)):
    if(sys.argv[x]=='-i'):
        face=sys.argv[x+1]
        x+=1
    elif(sys.argv[x]=='-r'):
        prevdump=sys.argv[x+1]
        x+=1
    elif(sys.argv[x] and len(sys.argv)>1):
        tbf=sys.argv[x]
    x+=1
load_layer("http")
load_layer("tls")
if(prevdump):
    packets=rdpcap(prevdump)
    for p in packets:
        requests(p)
    sys.exit(0)
try:
    if(not tbf) and (not face):
        sniff(prn=requests)
    elif(face and (not tbf)):
        sniff(iface=face,prn=requests)
    elif(tbf and (not face)):
        sniff(filter=tbf,prn=requests)
    else:
        sniff(filter=tbf,iface=face,prn=requests)
except:
    print("Exception: Please ensure Interface is valid & filter expression is valid. \n\n")
