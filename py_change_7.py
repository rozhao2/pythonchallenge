#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     21/08/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
# http://www.pythonchallenge.com/pc/def/oxygen.html
#-------------------------------------------------------------------------------
from PIL import Image

def main():
    img = Image.open("D:/temp/oxygen.png")
    width = img.size[0]
    mark = -1
    a = []
    for i in range(0,607):
        pix = img.getpixel((i,45))
        if mark != pix[0]:
            mark = pix[0]
            print mark,
            a.append(chr(mark))
    print ''.join(a)
    pass

def change():
    a =[105,110,116,101,103,114,105,116,121]
    b = []
    for i in a:
        b.append(chr(i))
    print ''.join(b)


if __name__ == '__main__':
    change()
