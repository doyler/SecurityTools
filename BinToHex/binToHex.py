# -*- coding: utf-8 -*-

#!/usr/bin/env python
if __name__ == "__main__":
 
	shellcode = "\""
	ctr = 1
	maxlen = 15
 
	for b in open("win-exec-calc-shellcode.bin", "rb").read():
		shellcode += "\\x" + b.encode("hex")
		if ctr == maxlen:
			shellcode += "\" +\n\""
			ctr = 0
		ctr += 1
	shellcode += "\""
	print(shellcode)
