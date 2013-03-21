import string,re,zipfile,os

prefixUrl = 'F://6/python challange/channel/'
suffixUrl = '.txt'
zip_file = zipfile.ZipFile(r'F://6/python challange/channel.zip','r')
comments = ''
num = '90052'
numlist = []

def getNum(url):
	f = open(url,'r')
	str = ''

	for line in f:
		str = "%s%s" %(str,line)
	#print str
	f.close()
	return re.findall(r'\d+',str)

def getComments():
		global comments
		for p,d,f in os.walk(prefixUrl):
			for txtfile in f:
				comments += zip_file.getinfo(txtfile).comment


if __name__ == '__main__':
	while True:
		comments += zip_file.getinfo(num + suffixUrl).comment
		url = prefixUrl + num + suffixUrl
		nums = getNum(url)
		if nums:
			num = nums[0]
		else:
			break

	print comments