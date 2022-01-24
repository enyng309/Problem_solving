# 섬의 개수
from collections import deque
from sys import stdin

def BFS(x, y):
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0

  while queue:
    now_x, now_y = queue.popleft()
    
    for i in range(8):
      width = now_x + dx[i]
      height = now_y + dy[i]
      
      if 0 <= width < h and 0 <= height < w and graph[width][height] == 1:
        graph[width][height] = 0
        queue.append((width, height))

dx = [1, -1, 0, 0, -1, -1, 1, 1] # 오른쪽, 왼쪽, 아래, 위
dy = [0, 0, 1, -1, -1, 1, -1, 1]

while True:
  w, h = map(int, stdin.readline().split()) # 너비 높이

  if w == 0 and h == 0:
    break

  graph = [list(map(int, input().split())) for _ in range(h)]

  cnt = 0
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        # 탐색
        BFS(i, j)
        cnt += 1

  print(cnt)