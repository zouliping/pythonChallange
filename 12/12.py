f = open(r'F:/6/python challange/12/evil2.gfx','rb')
content = f.read()
f.close()

for i in range(5):
	sf = open(r'F:/6/python challange/12/%d.jpg' % i,'wb')
	sf.write(content[i::5])
	sf.close()
