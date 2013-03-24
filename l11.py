'''
Created on 2013-3-24

@author: GunBar
'''
import PIL
from PIL import Image ,ImageDraw
img = Image.open('cave.jpg')
size = img.size
mode = img.mode
print(size, mode)
datal = list(img.getdata())
img1 = Image.new(mode, (size[0]/2,size[1]/2), (255,255,255))
img2 = Image.new(mode, (size[0]/2,size[1]/2), (255,255,255))
img3 = Image.new(mode, (size[0]/2,size[1]/2), (255,255,255))
img4 = Image.new(mode, (size[0]/2,size[1]/2), (255,255,255))
for y in range(size[1]/2):
    for x in range(size[0]/2):
        img1.putpixel((x,y), img.getpixel((2*x+1,2*y)))
        img2.putpixel((x,y), img.getpixel((2*x,2*y+1)))
        img3.putpixel((x,y), img.getpixel((2*x+1,2*y+1)))
        img4.putpixel((x,y), img.getpixel((2*x,2*y)))
        #=======================================================================
        # if y%2 == 0:
        #    img1.putpixel((x,y), img.getpixel((2*x+1,y)))
        # else:
        #    img2.putpixel((x,y), img.getpixel((2*x,y))) 
        #=======================================================================
#img1.show()
img4.show()

if __name__ == '__main__':
    pass