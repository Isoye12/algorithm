N = int(input())  # 목표 숫자 N 입력
result = 0        # 생성자를 찾지 못할 겨우 0으로 초기화

# 생성자는 N보다 최대 9 * (자리수)만큼 작을 수 있으므로
# 탐색은 N - 9 * (자리수)부터 시작 (단, 1보다 작으면 1부터 시작)
start = max(1, N - 9 * len(str(N))) 

# start부터 N-1까지 모든 수를 생성자 후보로 검사
for M in range(start, N): 
    sum_digits = 0 # 각 자리수의 합을 저장할 변수
    temp = M       # M 값을 나누며 자릿수를 구하기 위한 임시 변수

    # 각 자리수의 합 계산
    while temp > 0:
        sum_digits += temp % 10
        temp //= 10
    
    # 생성자 판별: M + (M의 자리수 합) == N이면
    if M + sum_digits == N:
        result = M  # 생성자 저장
        break       # 가장 작은 생성자를 찾았으므로 종료

print(result)