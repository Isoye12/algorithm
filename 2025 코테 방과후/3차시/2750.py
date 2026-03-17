def partition(arr, left, right):
    pivot = arr[left]
    low = left
    high = right + 1

    while True:
        while True:
            low += 1
            if low > right or arr[low] >= pivot:
                break

        while True:
            high -= 1
            if high < left or arr[high] <= pivot:
                break

        if low < high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
        else:
            temp = arr[left]
            arr[left] = arr[high]
            arr[high] = temp
            return high
        
def quick_sort(arr, left, right):
    if left < right:
      q = partition(arr, left, right)
      quick_sort(arr, left, q - 1)
      quick_sort(arr, q + 1, right)

n = int(input())
arr = [int(input()) for _ in range(n)]
quick_sort(arr, 0, n - 1)
for i in arr:
    print(i)