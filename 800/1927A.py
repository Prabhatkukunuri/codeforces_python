loop=int(input())
while loop>0:
    n=int(input())
    string=input()
    holder=[]
    for i in range(n):
        if string[i]=='B':
            holder.append(i)
    print((int(holder[-1])-int(holder[0]))+1)
    loop-=1
