import bs4
import re
import requests
import shutil
import sys
from urllib import urlopen

links = []
origLinks = []

# https://stackoverflow.com/questions/18042661/using-bs4-to-extract-text-in-html-files
page = urlopen('posts.txt').read().decode('utf-8')
soup = bs4.BeautifulSoup(page, "html.parser")
for node in soup.findAll('img'):
    #print(node['src'])
    links.append(node['src'])

# https://docs.python.org/3.4/library/re.html
for link in links:
    if re.search("-[0-9]*x[0-9]*\.jpg", link):
        origLinks.append(re.sub("-[0-9]*x[0-9]*\.jpg", ".jpg", link))
    else:
        origLinks.append(link)

# https://www.dev2qa.com/how-to-download-image-file-from-url-use-python-requests-or-wget-module/
for link in origLinks:
    filename = ""
    if link.find('/'):
        filename = link.rsplit('/', 1)[1]

    resp = requests.get(link, stream=True)
    localFile = open(filename, 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, localFile)
    del resp