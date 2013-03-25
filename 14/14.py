import Image

im = Image.open('wire.png')
newIm = Image.new(im.mode,(100,100))

doubled_steps = 200
directions = [(1,0),(0,1),(-1,0),(0,-1)]
x,y,pix = -1,0,0

while doubled_steps//2 > 0:
	for d in directions:
		steps = doubled_steps // 2
		for i in range(steps):
			x,y = x+d[0],y+d[1]
			newIm.putpixel((x,y),im.getpixel((pix,0)))
			pix += 1
		doubled_steps -= 1

newIm.save('newWire.png')