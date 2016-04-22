import zipfile
from time import time

def main():
    try:
        myZip = zipfile.ZipFile("secret.zip")
    except zipfile.BadZipfile:
        print "[!] There was an error opening your zip file."
        return

    password = ''
    
    timeStart = time()
    with open("10_million_password_list_top_10000.txt", "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                myZip.extractall(pwd = password)
                totalTime = time() - timeStart
                print "\nPassword cracked: %s\n" % password
                print "%i password attempts per second." % (pass_count/totalTime)
                return
            except Exception as e:
                if str(e[0]) == 'Bad password for file':
                    pass # TODO: properly handle exceptions?
                elif 'Error -3 while decompressing' in str(e[0]):
                    pass # TODO: properly handle exceptions?
                else:
                    print e
        print "Sorry, password not found."

if __name__ == '__main__':
	main()
