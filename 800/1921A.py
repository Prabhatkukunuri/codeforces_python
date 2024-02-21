#python code to calculate te area of a square
loop=int(input())
while loop > 0 :
    x1, y1 =input().split()
    x2, y2 =input().split()
    x3, y3 =input().split()
    x4, y4 =input().split()
    if int(x1)==int(x2):
        s=int(y1)-int(y2)
    if int(x1)==int(x3):
        s=int(y1)-int(y3)
    if int(x1)==int(x4):
        s=int(y1)-int(y4)
    print(s**2)
    loop +=-1   
    
