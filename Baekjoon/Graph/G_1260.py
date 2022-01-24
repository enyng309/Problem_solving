# DFS와 BFS
from collections import deque

N, M, V = map(int, input().split())
# N + 1 개 만큼의 공간을 만들어서 graph[N]이 N번 정점을 나타내도록 한다
graph = [[] for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
  graph[x].sort()
  graph[y].sort()

visited = [0 for _ in range(N+1)]

def DFS(graph, start, visited):
  visited[start] = 1  # 1: visit, 0: not
  print(start, end=' ')
  for node in graph[start]:
    if visited[node] == 0:
      DFS(graph, node, visited)

def BFS(graph, start):
  visited = [0] * (N + 1)
  queue = deque()
  
  visited[start] = 1  # 1: visit, 0: not
  queue.append(start)

  while queue:
    current = queue.popleft()
    print(current, end=' ')

    for node in graph[current]:
      if visited[node] == 0:
        visited[node] = 1
        queue.append(node)

def DFS2(graph, start):
  visited = [0 for _ in range(N+1)]
  stack = deque()

  visited[start] = 1  # 0: not, 1: peek, 2: visit
  stack.append(start)

  while stack:
    current = stack.pop()
    print(current, end=' ')
    visited[current] = 2
    
    for node in graph[current]:
      if visited[node] == 0:
        visited[node] = 1
        stack.append(node)

DFS(graph, V, visited)
print()
BFS(graph, V)
