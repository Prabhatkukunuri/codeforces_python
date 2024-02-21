loop=int(input())
while loop>0:
    x1,y1=input().split()
    x1=int(x1)
    y1=int(y1)
    checker=False
    if x1%2==0:
        if x1/2!=y1:
            checker=True
    if checker==False:
        if y1%2==0:
            if y1/2!=x1:
                checker=True
    if checker==True:
        print('YES')
    else:
        print('NO')
    loop-=1
