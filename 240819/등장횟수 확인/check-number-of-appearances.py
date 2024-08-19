# 짝수의 개수를 저장할 변수
even_count = 0

# 5개의 숫자를 입력받고 짝수의 개수를 카운트
for _ in range(5):
    number = int(input())
    # 짝수인지 확인
    if number % 2 == 0:
        even_count += 1

# 짝수의 개수를 출력
print(even_count)