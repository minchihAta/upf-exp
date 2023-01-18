#!/usr/bin/python
#coding=UTF-8

"""
TCP Client to collect P4 rate-show
"""

import socket
import time
import StringIO
host = "localhost"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
time.sleep(0.05)
res = client.recv(32768)
client.send("ucli\n")
time.sleep(0.05)
res = client.recv(32768)
client.send("rate-period 1\n")
rx = {}
tx = {}
times = 0
while times < 500000:
    client.send("rate-show\n")
    time.sleep(1)
    res = client.recv(32768)
    title = True
    buf = StringIO.StringIO(res)
    for line in buf.readlines():
        c = line.split("|")
        if len(c) == 12 and title is True:
            title = False
        elif len(c) == 12:
            if c[2] not in rx:
                rx[c[2]] = []
                tx[c[2]] = []
            rx[c[2]].append(c[8])
            tx[c[2]].append(c[9])
            rate = c[2] + " " + c[8] + " " + c[9] + ":" + str(times)
            print(rate)
    print("\n")
    times += 1

    for key,val in rx.items():
        f = open("data/rx-"+key, "w")
        f.write(str(val).strip("[]").replace(',','\n').replace(' ','').replace('\'',''))
        f.close()

    for key,val in tx.items():
        f = open("data/tx-"+key, "w")
        f.write(str(val).strip("[]").replace(',','\n').replace(' ','').replace('\'',''))
        f.close()

print(rx)
print(tx)

for key,val in rx.items():
    f = open("data/rx-"+key, "w")
    f.write(str(val).strip("[]").replace(',','\n').replace(' ','').replace('\'',''))
    f.close()

for key,val in tx.items():
    f = open("data/tx-"+key, "w")
    f.write(str(val).strip("[]").replace(',','\n').replace(' ','').replace('\'',''))
    f.close()

