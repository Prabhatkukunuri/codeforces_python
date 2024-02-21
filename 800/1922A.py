loop=int(input())
while loop>0:
    n = int(input())
    a = input()
    b = input()
    c = input()
    i = 0
    check=False
    while i<n:
        if a[i]!=c[i] and b[i]!=c[i]:
            check=True
            break
        i=i+1
    if check:
        print('YES')
    else:
        print('NO')
    loop=loop-1
