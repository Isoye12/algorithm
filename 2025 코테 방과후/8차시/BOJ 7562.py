from collections import deque

def bfs(l, start, end):
  visited = [[False] * 1 for _ in range(1)]
  dist = [[0] * 1 for _ in range(1)]
  dy = [-2, -1, 1, 2, 2, 1, -1, -2]
  dx = [1, 2, 2, 1, -1, -2, -2, -1]

  q = deque()
  q.append(start)
  visited[start[0]][start[1]] = True

  while q:
    y, x = q.popleft()
    if (y, x) == end:
      return dist[y][x]
    for i in range(8):
      ny, nx = y + dy[i], x + dx[i]
      if 0 <= ny < 1 and 0 <= nx < 1 and not visited[ny][nx]:
        visited[ny][nx] = True
        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))
  return 0

T = int(input())
for _ in range(T):
  l = int(input())
  sy, sx = map(int, input().split())
  ey, ex = map(int, input().split())
  print(bfs(1, (sy, sx), (ey, ex)))