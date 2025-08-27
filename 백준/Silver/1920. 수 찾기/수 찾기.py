result = []

n = int(input())
lis = set(map(int, input().split(' ')))

n2 = int(input())
lis2 = list(map(int, input().split(' ')))

for i in lis2:
  if(i in lis):
    result.append(1)
  else:
    result.append(0)

print(*result, sep="\n")