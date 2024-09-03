n= []
while True:
    k=int(input())
    if k<20 or k>=30:
        break
    n.append(k)
if n:
    average = sum(n)/len(n)
    print(f'{average:.2f}')