# 백준 1920번
# 이진 탐색 함수 정의: 정렬된 배열(array)에서 target 값을 찾는 함수

def binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return True
    elif arr[mid] < target:
      left = mid + 1 
    else:
      right = mid - 1
  return False

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
isIn = list(map(int, input().split()))

for num in isIn:
  print(1 if binary_search(a, num) else 0)