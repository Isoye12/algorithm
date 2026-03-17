n = int(input())
words = [input() for _ in range(n)]

words = list(set(words))

words.sort(key=lambda x: (len(x), x))
# `len(x)` 기준 오름차순, `x` 기준 오름차순

for word in words:
  print(word)