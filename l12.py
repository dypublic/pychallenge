'''
Created on 2013-4-2

@author: GunBar
'''
from io import StringIO
with open("evil2.gfx", mode='br') as f:
    content = f.read()
    for i in range(5):
        piece = content[i::5]
        with open("%d.jpg"%i,mode = 'bw') as files:
            files.write(piece)
         
if __name__ == '__main__':
    pass