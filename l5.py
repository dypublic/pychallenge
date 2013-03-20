'''
Created on 2013-3-20

@author: GunBar
'''
import urllib
import pickle
import pprint
from urllib import request
res = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(res)
pprint.pprint(data)
for list in data:
    temp = ''
    for item in list:
        temp += item[0] * item[1]
        #print(item[0] * item[1])
    print(temp+'\n')

if __name__ == '__main__':
    pass