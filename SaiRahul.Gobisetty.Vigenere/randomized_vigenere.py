#########################################################
#Name: Sai Rahul Gobisetty
#Class: CMPS 5363 Cryptography
#Date: 28th July 2015
#Program 2 - Randomized Vigenere Cipher
#randomized_vigenere.py
#########################################################

import random

#generating unique key using seed
def keywordFromSeed(seed):
	Letters = []
	while seed > 0:
		Letters.insert(0,chr((seed % 1000) % 95 + 32))
		seed = seed // 1000
	key=''.join(Letters)
	return key

#Encrypting plain text message to cipher text
def encrypt(plain_text_message,seed):
	keyWord=keywordFromSeed(seed)
	symbols=""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
	vigenere=buildVigenere(symbols,seed)
	cipher_text_message=[0 for i in range(len(plain_text_message))]
	n=len(symbols)
	p=len(plain_text_message)
	k=len(keyWord)
	x=0
	i=0
	while(x<p):
		
		for j in range(n):
			if(keyWord[i]==vigenere[j][0] and x<p):
				
				cipher_text_message[x]=vigenere[j][(ord(plain_text_message[x]))-32]
		x=x+1
		i=i+1
		i=i%k
	
	return ''.join(cipher_text_message)
	
#Decrypting cipher text message to plain text
def decrypt(cipher_text_message,seed):
	keyWord=keywordFromSeed(seed)
	symbols=""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
	vigenere=buildVigenere(symbols,seed)
	plain_text_message=[0 for i in range(len(cipher_text_message))]
	n=len(symbols)
	p=len(cipher_text_message)
	k=len(keyWord)
	x=0
	l=0
	while(x<p):
		for i in range(n):
			if vigenere[i][0]==keyWord[l] and x<p:
				for j in range(n):
					if(vigenere[i][j]==cipher_text_message[x]):
						plain_text_message[x]=chr(j+32)
		x=x+1
		l=l+1
		l=l%k
	return ''.join(plain_text_message)
	
#build randomized vigenere table using seed
def buildVigenere(symbols,seed):
	random.seed(seed)
	n=len(symbols)
	vigenere=[[0 for i in range(n)] for i in range(n)]
	
	symbols=list(symbols)
	random.shuffle(symbols)
	symbols=''.join(symbols)
	for sym in symbols:
		random.seed(seed)
		myList=[]
		for i in range(n):
			r=random.randrange(n)
			if r not in myList:
				myList.append(r)
			else:
				while(r in myList):
					r=random.randrange(n)
				myList.append(r)
			while(vigenere[i][r] != 0):
				r = (r + 1) % n
			vigenere[i][r] = sym
	return vigenere