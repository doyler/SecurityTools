#!/usr/bin/python

import math
import socket
import sys

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

def roundup(x, base=10):
    return int(math.ceil(x / (base + 0.0))) * base

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
s.connect(server_address)

try:
    found = False
    secret = ""

    secretLen = 0
    #prependChars = "ENCRYPT:"
    prependChars = ""

    message = "A"
    s.sendall(message)
    data = s.recv(2048)
    output = list(chunkstring(data, 32))
    initialLen = len(output)

    curLen = 0

    while (curLen <= initialLen):
        message += "A"
        s.sendall(message)
        data = s.recv(2048)
        output = list(chunkstring(data, 32))
        curLen = len(output)

    extra = len(message) - 1

    secretLen = ((curLen - 1) * 16) - extra - len(prependChars)

    print("SECRETLEN: " + str(secretLen))

    while not found:
        initialBlock = "A" * (16 - len(prependChars))
        fullLen = roundup(secretLen, 16)
        prepend = "B" * (fullLen - len(secret) - 1)
        message1 = initialBlock + prepend

        s.sendall(message1)
        data = s.recv(8192)
        initialReturn = list(chunkstring(data, 32))
        #print("INITIAL: " + str(initialReturn))

        for i in range(33, 127):
            message2 = message1 + secret + chr(i)
            s.sendall(message2)
            data = s.recv(8192)
            oracle = list(chunkstring(data, 32))
            #print("ORACLE: " + str(oracle))
            compareBlock = (len(prependChars + message2) / 16) - 1
            #print("COMPARE = " + str(compareBlock))
            if oracle[compareBlock] == initialReturn[compareBlock]:
                secret += chr(i)
                #print("LENGTH: " + str(len(secret)))
                #print("SECRET: " + secret)
                #print("INITIAL: " + str(initialReturn))
                #print("ORACLE: " + str(oracle))
                if len(secret) == secretLen:
                    found = True
                    print(secret)
                break
    
finally:
    s.close()
