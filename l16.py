'''
Created on 2013-4-7

@author: GunBar
'''
import Image
from PIL import Image ,ImageDraw
from pprint import pprint

img = Image.open('mozart.gif')
size = img.size
img4 = Image.new(img.mode, size)
for y in range(size[1]):
    line = [ img.getpixel((i,y)) for i in range(size[0]) ]
    index = line.index(195 )
    line = line[index:] + line[:index]
    for x in range(size[0]):
        img4.putpixel((x,y),  line[x])
        #img4[x,y] = line[x]

img4.show()
if __name__ == '__main__':
    pass