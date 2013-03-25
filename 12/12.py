f = open(r'evil2.gfx','rb')
content = f.read()
f.close()

for i in range(5):
	sf = open(r'%d.jpg' % i,'wb')
	sf.write(content[i::5])
	sf.close()
