import socket

hosts = ["192.168.1.1", "192.168.2.1", "192.168.2.2", "192.168.2.10"]

lowPort = 1
highPort = 65535
ports = [22, 23, 80, 443, 445, 3389]
#ports = range(lowPort, highPort)

for host in hosts:
    for port in ports:
        try:
            print "[+] Connecting to " + host + ":" + str(port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            result = s.connect_ex((host, port))
            #banner = s.recv(1024) # Will cause a timeout w/o a response
            if result == 0:
                print "  [*] Port " + str(port) + " open!"
            s.close()
        except:
            pass
