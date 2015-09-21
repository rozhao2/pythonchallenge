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
import os
import os.path
import zipfile

def main():
    f = open("D:/channel/90052.txt")
    while True:
        content = f.read()

        if content.startswith("Next nothing is "):
            content = content.replace("Next nothing is ","")
            print content
            f = open("D:/channel/%s.txt" % content)
        else:
            break

    pass

def test():
    f = open("D:/files.txt")
    z = zipfile.ZipFile("D:/channel.zip")
    comment_map = {}
    for filename in z.namelist():
        comment_map[filename] = z.getinfo(filename).comment
    arr = []
    for fn in f.readlines():
        fn = fn.replace("\n","")
        fn = fn+".txt"
        arr.append(comment_map[fn])
    print ''.join(arr)

if __name__ == '__main__':
    test()
