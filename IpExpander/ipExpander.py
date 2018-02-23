from netaddr import *
import pprint

def isIP(inLine):
    try:
        ip = IPAddress(inLine)
    except:
        return False
    return True

def isCIDR(inLine):
    try:
        ip_list = IPNetwork(inLine)
    except:
        return False
    return True

def expandCIDR(inCIDR):
    return list(IPNetwork(inCIDR))

def isRange(inLine):
    if "-" in inLine:
        return True
    else:
        return False

def expandRange(inRange):
    splitRange = inRange.split("-")
    try:
        startIP = IPAddress(splitRange[0])
    except:
        print "***** ERROR *****: " + splitRange[0]

    endRange = splitRange[1]

    try:
        int(endRange)
        if int(endRange) <= 255:
            endNet = str(IPNetwork(str(startIP).strip() + '/24').network)
            endIP = endNet.rsplit(".", 1)[0] + "." + endRange    
        else:
            print "***** ERROR *****: " + endRange
    except ValueError:
        try:
            endIP = IPAddress(endRange)
        except:
            print "***** ERROR *****: " + splitRange[0]

    return list(iter_iprange(startIP, endIP))

def getTargets(inFile):
    with open(inFile) as f:
        lines = f.readlines()
    return lines

def newFile(outList, fileName):
    with open(fileName.split(".")[0] + "-expanded.txt", "w") as text_file:
        for addr in outList:
            text_file.write(str(addr) + "\n")

def main():
    inFile = "external-targets.txt"
    lines = getTargets(inFile)

    finalList = []

    for line in lines:
        line = line.strip()
        if isIP(line):
            finalList.append(IPAddress(line))
        elif isCIDR(line):
            expanded = expandCIDR(line)
            finalList.extend(expanded)
        elif isRange(line):
            expanded = expandRange(line)
            finalList.extend(expanded)
        else:
            print "***** ERROR *****: " + line

    newFile(sorted(finalList), inFile)

if __name__ == '__main__':
    main()