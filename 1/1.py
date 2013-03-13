import string
d = {}
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
nstr = ""
s = "map"

for c in string.lowercase:
	num = ord(c) + 2
	nc = chr(num%97%26 + 97)
	d[c] = nc
print d

for key in s:
        if key in d.keys():
            nstr += d[key]
        else:
            nstr += key

print nstr

