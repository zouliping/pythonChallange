str = ''
wordlist = []

def getString():
	global str
	f = open(r'F://6/python challange/2.txt','r')

	for line in f:
		str = "%s%s" %(str,line)
	f.close()

def findChr():
	global wordlist
	for chr in str:
		if chr not in wordlist:
			wordlist.append(chr)

if __name__ == '__main__': 
	getString()
	findChr()

	for c in wordlist:
		print c,"	",str.count(c)
