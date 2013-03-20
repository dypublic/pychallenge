'''
Created on 2013-3-21

@author: GunBar
'''
import urllib
import pickle
import pprint
import zipfile
import re
name = '90052'
with zipfile.ZipFile('channel.zip', 'a') as myzip:
    res = ''
    for i in range(len(myzip.namelist() )):
        resstr = myzip.open(name+'.txt',mode='r').readline()
        print(resstr)
        res += str(myzip.getinfo(name+'.txt').comment,encoding = 'ascii')
        try:
            name = re.search(r'Next nothing is (\d+)',str(resstr)).group(1)
        except:
            break
    print(res) 

#print(zipfile.is_zipfile(res))
if __name__ == '__main__':
    pass