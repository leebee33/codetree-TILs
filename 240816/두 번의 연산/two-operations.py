a = int(input())
if a%2 !=0:
    if (a+3)%3==0:
        print (f'{(a+3)//3}')

if a%2==0:
    if a%3==0:
        print(f'{a//3}')