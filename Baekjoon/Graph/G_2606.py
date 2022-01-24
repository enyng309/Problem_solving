# 바이러스
from collections import deque
from sys import stdin

computer = int(stdin.readline())
edge = int(stdin.readline())

# N + 1 개 만큼의 공간을 만들어서 graph[N]이 N번 정점을 나타내도록 한다
graph = [[] for _ in range(computer+1)]

for _ in range(edge):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [0 for _ in range(computer+1)]

def DFS2(graph, start):
  visited = [0 for _ in range(computer+1)]
  cnt = 0
  stack = deque()

  visited[start] = 1  # 0: not, 1: peek, 2: visit
  stack.append(start)

  while stack:
    current = stack.pop()
    visited[current] = 2
    cnt += 1
    
    for node in graph[current]:
      if visited[node] == 0:
        visited[node] = 1
        stack.append(node)
  return cnt

print(DFS2(graph, 1) - 1)
