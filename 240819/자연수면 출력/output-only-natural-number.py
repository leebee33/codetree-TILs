a,b=map(int,input().split())

if a > 0:
    # a를 b번 반복하여 출력
    result = str(a) * b
    print(result, end=' ')
else:
    print(0)