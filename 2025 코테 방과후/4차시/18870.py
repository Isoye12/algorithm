n = int(input())
arr = list(map(int, input().split()))
dict_arr = {val: i for i, val in enumerate(sorted(set(arr)))}
res = [dict_arr[val] for val in arr]
print(*res)