import urllib2
import re

originUrl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = []
num.append('63579')
        
for i in range(400):
        req = urllib2.Request(url=originUrl+str(num[i]))
        fd = urllib2.urlopen(req)
        tmp = fd.read()
        print tmp
        num.append(re.findall(r'\d+',tmp)[0])
	
