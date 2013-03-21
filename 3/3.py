import re

linelist = []
req = r"[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]"

def getString():
	global linelist
	f = open(r'F://6/python challange/3.txt','r')

	for line in f:
		linelist.append(line)
	f.close()
	
if __name__ == '__main__':
	getString()
	for line in linelist:
		result = re.findall(req,line)
		if result:
			print result
