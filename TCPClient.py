'''
Parth Mistry
prm46
Section 003
'''

import socket
from _socket import AF_INET, SOCK_STREAM
from socket import timeout as TimeoutException
import sys
import struct
import os

s = socket.socket(AF_INET, SOCK_STREAM)

if (len(sys.argv) == 2):
    URL = sys.argv[1]
else:
    URL = "localhost:12000/filename.html"
i = URL.find(":")
hostname = URL[:i]
if hostname == "localhost":
    SERVERIP = "127.0.0.1"
    
j = URL.find("/")
SERVERPORT = URL[i+1:j]

FILE = URL[j+1:]

cachedfileName = "cached" + FILE

if os.path.exists(cachedfileName):
    s.connect((SERVERIP, int(SERVERPORT)))
    s.sendall("GET / HTTP/1.1\r\nHost: " + hostname + "\r\nIf-Modified-Since: " + os.path.getmtime(cachedfileName) + "\r\n\r\n")
    resp = s.recvfrom(4096)
    resp = "hello, world!\nhow are you?"
    if resp == "The file was not updated since the last modification.":
        print(resp)
    else:
        print(resp)
        f = open(cachedfileName, "w")
        f.write(resp)
        f.close()
else:
    s.connect((SERVERIP, int(SERVERPORT)))
    s.sendall("GET / HTTP/1.1\r\nHost: " + hostname + "\r\n\r\n")
    resp = s.recvfrom(4096)
    resp = "hello, world!\nhow are you?"
    print(resp)
    f = open(cachedfileName, "w")
    f.write(resp)
    f.close()
    

s.close()