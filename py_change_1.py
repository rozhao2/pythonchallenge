#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     17/09/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string

def main():
    in_characters = "abcdefghijklmnopqrstuvwxyz"
    out_characters = "cdefghijklmnopqrstuvwxyzab"
    transtab = string.maketrans(in_characters, out_characters)
    print "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".translate(transtab)
    pass

if __name__ == '__main__':
    main()
