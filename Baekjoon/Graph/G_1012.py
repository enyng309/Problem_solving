# 유기농 배추
from collections import deque
from sys import stdin

def BFS(x, y):
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0

  while queue:
    now_x, now_y = queue.popleft()
    
    for i in range(4):
      w = now_x + dx[i]
      h = now_y + dy[i]
      
      if 0 <= w < N and 0 <= h < M and graph[w][h] == 1:
        graph[w][h] = 0
        queue.append((w, h))

T = int(stdin.readline()) # test 개수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(T):
  M, N, K = map(int, stdin.readline().split())  # 밭의 가로, 세로, 위치 개수
  graph = [ [0] * M for _ in range(N)]

  for _ in range(K):
    x, y = map(int, stdin.readline().split())
    graph[y][x] = 1
  
  worm = 0
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1:
        # 탐색
        BFS(i, j)
        worm += 1

  print(worm)