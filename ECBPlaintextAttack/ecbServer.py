#!/usr/bin/python

from Crypto.Cipher import AES
import socket
import sys
import random
import string

blockSize = 16
encKey = "ENCRYPTIONKEY123"
secret = "mys3cretP@ssword!"
prepend = ""
#prepend = "ENCRYPT:"
chars = string.ascii_letters + string.digits + string.punctuation
secret = ''.join(random.choice(chars) for _ in range(random.randint(1,1000)))

def pad(input):
	if (len(input) % blockSize == 0):
		return input
	else:
		extra = blockSize - (len(input) % blockSize)
		output = input + "\x00" * extra
		return output

def unpad(input):
	return input.rstrip("\x00")

def encrypt(input):
	if (input is None) or (len(input) == 0):
		print("Input text cannot be null or empty")

	toEncrypt = prepend + input + secret
	toEncrypt = pad(toEncrypt)
	cipher = AES.AESCipher(encKey, AES.MODE_ECB)
	cipherText = cipher.encrypt(toEncrypt)
	return cipherText.encode("hex")

def decrypt(input):
	if (input is None) or (len(input) == 0):
		print("Input text cannot be null or empty")

	encrypted = input.decode("hex")
	cipher = AES.AESCipher(encKey, AES.MODE_ECB)
	plainText = unpad(cipher.decrypt(encrypted))
	return plainText

def main():
	print("SECRET LENGTH: " + str(len(secret)))
	print("SECRET = " + secret)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	server_address = ('localhost', 10000)
	print("\nStarting up on %s port %s" % server_address)
	s.bind(server_address)

	s.listen(1)

	while True:
	   	connection, client_address = s.accept()

	   	try:
	   		while True:
	   			data = connection.recv(2048)
	   			if data:
	   				#print("DATA: " + data)
	   				input = data.rstrip()
	   				print("INPUT: " + input)
	   				print("HEX: " + input.encode("hex"))
	   				encrypted = encrypt(input)
	   				print("ENCRYPTED: " + encrypted)
	   				connection.send(encrypted)
	   			else:
	   				break
	   	finally:
	   		connection.close()
    
if __name__ == "__main__":
    main()
