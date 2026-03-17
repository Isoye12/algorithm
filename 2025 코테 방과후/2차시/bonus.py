from collections import deque

n, T = map(int, input().split())
q = deque()
result = []

for _ in range(n):
  q.append(list(input().split()))

while(len(q) >= 0):
  # 