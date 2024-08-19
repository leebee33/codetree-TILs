def division_count(n):
    count = 0  # 나누는 횟수 초기화
    i = 1  # 첫 번째 나누는 수
    
    while n > 1:
        n //= i  # n을 i로 나누고 몫을 n에 저장
        count += 1  # 나누는 횟수 증가
        i += 1  # 나누는 수 증가
    
    return count

# 예시 실행
n = int(input())
result = division_count(n)
print(result)