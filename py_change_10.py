
def caculate(n):
    a=[]
    if n == 1:
        a.append(1)
        return a
    else:
        return caculate(n-1)

if __name__ == '__main__':
    caculate(31)