'''
Parth Mistry
prm46
Section 003
'''

import socket
from _socket import AF_INET, SOCK_STREAM
import random
import struct

f = open("filename.html", "r")

SERVERIP = "127.0.0.1"
SERVERPORT = 12000

s = socket.socket(AF_INET, SOCK_STREAM)

s.bind((SERVERIP, SERVERPORT))

print ("The server is ready to receive on port: " + str(SERVERPORT))

while (True):
    rand = random.randint(1, 11)
    recvdMsg, clientAddr = s.recvfrom(2048)
    CLIENTIP = str(clientAddr[0])
    CLIENTPORT = str(clientAddr[1])
    val = struct.unpack('ii', recvdMsg)
    #print(val)
    if (rand < 4):
        print("Message with sequence number " + str(val[1]) + " dropped")
        #print("if")
    else:
        print("Responding to ping request with sequence number " + str(val[1]))
        delay = random.uniform(0.0, 1.0)
        s.sendto(struct.pack('ii', 2, val[1]), clientAddr)