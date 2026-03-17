n = int(input())
lis = []
for i in range(n):
  lis.append(list(map(int, input().split())))

lis.sort(key=lambda point: (point[0], point[1])) 
# `x[0]` 기준 오름차순, `x[1]` 기준 오름차순

for i in lis:
  print(i[0], i[1])