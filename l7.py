'''
Created on 2013-3-22

@author: GunBar
'''
import urllib
import PIL
from PIL import Image
#myurl = 'http://www.pythonchallenge.com/pc/def/oxygen.png'

#p = urllib.urlopen(myurl)
#print(p)
img = Image.open('oxygen.png')
res = img.getdata()
a = []
for pix in res:
    if pix[0] == pix[1] == pix[2]:
        a.append(chr(pix[0]))
print(a)
b = [c for i,c in enumerate(a) if i%7 == 0]
b = "".join(b)
print(b)
#===============================================================================
# b += a[0]
# i = 0
# for c in a:
#    if c != b[-1]:
#        b += c
#        i = 0
#    else:
#        i+=1
#        if i == 7:
#            i = 0
#            b += c
# b = "".join(b)
# print(b)
# print(chr(43))
# print(ord('a'))
#===============================================================================
res = [105, 110, 116, 101, 103, 114, 105, 116, 121]
a = [chr(c) for i,c in enumerate(res)]
print("".join(a))
if __name__ == '__main__':
    pass