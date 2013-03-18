'''
Created on Mar 18, 2013

@author: daiyue
'''
import urllib
import re

myurl = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
change = '85501'
for i in range(400):
    p = urllib.urlopen(myurl+change)
    #print (p.read(), change)
    string = p.read()
    match = re.search(r"nothing is (\d+)$",string)
    if match:
        change = match.group(1)
    else:
        print(string)
        break
    #change = string.split()[-1]
#    if 'and noting' not in string :
#        print(string) 
#    print (change)
#print(p.read())
    
