n = int(input())
result = []

for i in range(n):
    n = int(input())
    if(n==0):
        result.pop()
    else:
        result.append(n)
print(sum(result))