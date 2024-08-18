b,a=map(int,input().split())

c=b
while c>=a:
    if c%2==0:
        print(c, end=' ')
    c-=1