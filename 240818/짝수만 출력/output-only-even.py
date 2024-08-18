a,b = map(int,input().split())

current = a
while current<=b:
    if current%2==0:
        print(current,end=' ')
        
    current+=1