'''
Created on 2013-4-3

@author: GunBar
'''
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print("%s" % str(proxy.phone('Bert')))


if __name__ == '__main__':
    pass