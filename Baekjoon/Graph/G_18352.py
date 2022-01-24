# 특정 거리의 도시 찾기
import heapq
from sys import stdin
import sys

# N: 도시 개수, M: 도로(edge) 개수, K: 거리 정보, X: 출발도시
N, M, K, X = map(int, stdin.readline().split()) 
inf = sys.maxsize
# N + 1 개 만큼의 공간을 만들어서 graph[N]이 N번 정점을 나타내도록 한다
graph = [[] for _ in range(N+1)]
distance = [inf] * (N + 1)

# make edge
for _ in range(M):
  x, y = map(int, stdin.readline().split())
  graph[x].append((y, 1))

def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0

  while queue:
    current_d, current_node = heapq.heappop(queue)
    if distance[current_node] < current_d: 
      continue
    for next_node in graph[current_node]:
      weight = current_d + next_node[1]
      if weight < distance[next_node[0]]:
        distance[next_node[0]] = weight
        heapq.heappush(queue, (weight, next_node[0]))    

dijkstra(X)
result = []

for i in range(1, N+1):
  if distance[i] == K:
    result.append(i)

if result:
  for i in result:
    print(i)

else:
  print(-1)
  