loop=int(input())
while loop>0:
    n , k =input().split()
    n=int(n)
    k=int(k)
    alphabets="abcdefghijklmnopqrstuvwxyz"
    answer=alphabets[:k]*n
    print(answer)
    loop-=1
