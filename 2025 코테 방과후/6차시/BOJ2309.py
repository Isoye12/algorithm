arr = [int(input()) for _ in range(9)]
total = sum(arr)
over = total - 100 # 초과된 키의 합

liar1 = liar2 = -1

# 두 난쟁이 찾기
# 브루트포스 알고리즘
for i in range(9):
    for j in range(i+1, 9):
        if arr[i] + arr[j] == over:
            liar1, liar2 = i, j
            break
    if liar1 != -1:
        break
    
# 진짜 난쟁이만 리스트에 담기
dwarfs = [arr[i] for i in range(9) if i != liar1 and i != liar2]
dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)