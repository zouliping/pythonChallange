import re

def describe(s):
	result = []
	for m in re.finditer(r'(\d)\1*',s):
		result.append(str(len(m.group(0))) + m.group(1))
	return ''.join(result)

if __name__ == '__main__':
	s = '1'
	for i in range(30):
		s = describe(s)
		print s

	print len(s)