#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     21/08/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pickle
import urllib2
def main():
    a = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").readlines()
    data = pickle.loads(''.join(a))
    for r in data:
        result = ''
        for s in r:
            result = result + s[0]*s[1]
        print result

if __name__ == '__main__':
    main()
