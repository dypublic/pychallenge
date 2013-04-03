'''
Created on 2013-4-3

@author: GunBar
'''
import calendar
import datetime

for year in range(1006,2012,10):
    if calendar.isleap(year):
        if  calendar.weekday(year, 1, 27) == calendar.TUESDAY:
            print year


if __name__ == '__main__':
    pass