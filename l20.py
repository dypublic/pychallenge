'''
Created on 2013-4-18

@author: GunBar
'''
import urllib
url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/unreal.jpg'

##Private info found
for i in [(30237,30337), (30284,30384), (30295,30395), (30313,30413),
          (2123456744,2123456788), (2123456712,2123456743)]:
    opener = urllib.FancyURLopener({})
    opener.addheader("range", "bytes=%d-%d" % i)
    f = opener.open(url)
    print f.read()

##Something hidden in this particular range.
opener = urllib.FancyURLopener({})
opener.addheader("range", "bytes=%d-%d" % (1152983631,1152983671))
f = opener.open(url)
print f.info()


open("20.zip", "w").write(f.read())
if __name__ == '__main__':
    pass