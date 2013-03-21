import Image

im = Image.open('F:/6/python challange/7/oxygen.png')
#print im.mode

y_begin = 0
while True:
	pix = im.getpixel((0,y_begin))
	if pix[0] == pix[1] == pix[2]:
		break
	y_begin += 1

x_end = 0

while True:
	pix = im.getpixel((x_end,y_begin))
	if not pix[0] == pix[1] == pix[2]:
		break
	x_end += 1

print x_end,y_begin

grayMessage = []
for i in range(0,x_end,7):
	grayMessage.append(chr(im.getpixel((i,y_begin))[0]))

print grayMessage
print ''.join(grayMessage)

message = [105,110,116,101,103,114,105,121]
print ''.join(chr(ch) for ch in message)