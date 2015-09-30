#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     29/09/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def calculate(n):
    a=[]
    a.append("1")
    for i in range(1, n):
        s=""
        temp_num = a[i-1][0]
        num_cnt = 1
        has_changed = False
        for j in range(1, len(a[i-1])):
            temp = a[i-1][j]
            if temp_num != temp:
                s=s+str(num_cnt)
                s=s+str(temp_num)
                temp_num = temp
                num_cnt = 1
            else:
                num_cnt += 1
        s=s+str(num_cnt)
        s=s+str(temp_num)
        a.append(s)
        print len(s),

def main():
    calculate(31)

if __name__ == '__main__':
    main()
