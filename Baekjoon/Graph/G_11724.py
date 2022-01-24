# 연결 요소의 개수
from collections import deque
from sys import stdin
import sys

sys.setrecursionlimit(10000)

N, M = map(int, stdin.readline().split())
# N + 1 개 만큼의 공간을 만들어서 graph[N]이 N번 정점을 나타내도록 한다
graph = [[] for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

visited = [0 for _ in range(N+1)]

def DFS(graph, start, visited):
  visited[start] = 1  # 1: visit, 0: not
  
  for node in graph[start]:
    if visited[node] == 0:
      DFS(graph, node, visited)

connect = 0

for i in range(1, len(visited)):
  if visited[i] == 0:
    connect += 1
    DFS(graph, i, visited)

print(connect)