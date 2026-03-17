# 택배의 무게
# 문제: 택배 상자 무게 맞추기
# 문제 설명
# 당신은 여러 개의 상자를 보유하고 있으며, 각 상자의 무게는 정해져 있다.
# 이 중에서 일부 상자를 골라 정확히 목표 무게 W을 만들고 싶다.
# 단, 같은 상자를 여러 번 사용할 수는 없다.
# 모든 가능한 조합을 시도해서 목표 무게를 만들 수 있는 경우가 있는지 판단하라

# 입력 형식
# N: 상자의 개수 (1 ≤ N ≤ 15)
# W: 목표 무게 (1 ≤ W ≤ 10,000)
# w₁ ... wₙ: 각 상자의 무게 (1 ≤ wᵢ ≤ 1,000)

# 출력 형식
# 목표 무게 W을 만들 수 있다면 → YES
# 만들 수 없다면 → NO

N, W = map(int, input().split())
weights = list(map(int, input().split()))

found = False

for i in range(1 << N):  # 0부터 2^N - 1까지 모든 부분집합을 나타내는 비트마스크
    total = 0
    for j in range(N):
        if i & (1 << j):  # j번째 상자가 선택되었는지 확인
            total += weights[j]
    if total == W:
        found = True
        break
    
print("YES" if found else "NO")