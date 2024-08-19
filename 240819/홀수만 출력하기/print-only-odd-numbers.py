N=int(input())
# N개의 줄에 걸쳐 정수를 입력받고 조건에 맞는 수를 저장하기 위한 리스트
result = []

# N개의 정수를 입력받고 조건에 맞는 수를 저장
for _ in range(N):
    number = int(input()) 
    # 홀수이면서 3의 배수인지 확인
    if number % 2 != 0 and number % 3 == 0:
        result.append(number)

# 결과 출력
for num in result:
    print(num)