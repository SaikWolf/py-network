#!/usr/bin/env python3
import os,sys,time,signal

def handle(sig,frame):
    print("Got sig:",sig)

SIG2NAME = dict((getattr(signal,n),n) for n in dir(signal) if n.startswith("SIG"))

for i in SIG2NAME.keys():
    print(i,int(i))
    if i in [0,19,9]:
        continue
    signal.signal(i,handle)

print(os.getpid())

while True:
    time.sleep(1.0)


