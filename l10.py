'''
Created on 2013-3-24

@author: GunBar
'''
from itertools import groupby
name = '1'
print(''.join("%d%s"%(len(list(g)),v) for v,g in groupby(name) ))
for i in range(30):
    name = ''.join("%d%s"%(len(list(g)),v) for v,g in groupby(name) )
    print(len(name))
print(len(name))
if __name__ == '__main__':
    pass