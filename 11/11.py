import Image

im = Image.open('F:/6/python challange/11/cave.jpg')
print im.size,im.mode

width = im.size[0]
height = im.size[1]

oddIm = Image.new(im.mode,(width/2,height/2))
evenIm = Image.new(im.mode,(width/2,height/2))

for x in range(1,width,2):
	for y in range(1,height,2):
		oddIm.putpixel((x/2,y/2),im.getpixel((x,y)))
		evenIm.putpixel(((x-1)/2,(y-1)/2),im.getpixel((x,y)))			
oddIm.save('odd.jpg')
evenIm.save('evenIm.jpg')
