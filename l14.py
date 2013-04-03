'''
Created on 2013-4-3

@author: GunBar
'''
import Image
from PIL import Image ,ImageDraw
from pprint import pprint
pos = []
for i in range(50):
    pos.extend(( (j,i) for j in range(i, 100-i)))
    #pprint( len(pos))
    pos.extend(( (99-i,j) for j in range(i+1, 100-i)))
    #pprint( len(pos))
    pos.extend(( (99-j, 99-i) for j in range(i+1, 100-i)))
    #pprint( len(pos))
    pos.extend(( (i,99-j) for j in range(i+1, 100-1-i)))
img = Image.open('wire.png')
img4 = Image.new(img.mode, (100,100))
for i in range(10000):
    try:
        img4.putpixel(pos[i], img.getpixel((i,0)))
    except IndexError ,e:
        print (i)
            
        #=======================================================================
        # if y%2 == 0:
        #    img1.putpixel((x,y), img.getpixel((2*x+1,y)))
        # else:
        #    img2.putpixel((x,y), img.getpixel((2*x,y))) 
        #=======================================================================
#img1.show()
img4.show()
pprint( len(pos))
if __name__ == '__main__':
    pass