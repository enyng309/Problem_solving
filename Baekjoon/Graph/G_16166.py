# 서울의 지하철
from collections import deque
from sys import stdin

def find_start(subwaylist): # find 0(start point) index
  loc_zero = []
  for i in range(len(subwaylist)):
    for j in range(len(subwaylist[i])):
      if subwaylist[i][j] == 0:
        loc_zero.append([i, j])
        break
      else:
        continue
  loc_zero = sum(loc_zero, [])
  return loc_zero

def find_destn(subwaylist, destination):
  loc_destn = []
  for i in range(len(subwaylist)):
    for j in range(len(subwaylist[i])):
      if subwaylist[i][j] == destination:
        loc_destn.append([i, j])
        break
      else:
        continue
  #loc_destn = sum(loc_destn, [])
  return loc_destn

def BFS(graph, start, dest):
  visited = list(graph)
  for i in range(len(graph)):
    for j in range(len(graph[i])):
      visited[i][j] = 0
  
  queue = deque()
  
  visited[loc_zero[0]][loc_zero[1]] = 1  # 1: visit, 0: not
  queue.append(start)

  while queue:
    current = queue.popleft()

    for node in graph[current]:
      if visited[node] == 0:
        visited[node] = 1
        queue.append(node)

N = int(input())
graph = []
for i in range(N):
  graph.append(list(map(int, stdin.readline().split())))

destination = int(input())
transfer = 0

line1 = graph[0][0]
del graph[0][0]
line2 = graph[1][0]
del graph[1][0]
line3 = graph[2][0]
del graph[2][0]


loc_zero = find_start(graph)
print(loc_zero)

loc_destn = find_destn(graph, destination)
print(loc_destn)

if loc_zero[0] == loc_destn[0]:
  print(transfer)





from collections import deque
n=int(input())
K=[[] for _ in range(n+1)]
S=[[] for _ in range(n+1)]
D=[float('inf')]*(n+1)
for i in range(1,n+1):
    a,*b=map(int,input().split())
    for j in range(len(b)):
        K[i].append(b[j])
for i in range(1,n+1):
    for j in range(len(K[i])):
        for x in range(i+1,n+1):
            for y in range(len(K[x])):
                if K[i][j]==K[x][y]:
                    S[i].append(x)
                    S[x].append(i)
q=deque()
for i in range(1,n+1):
    for j in range(len(K[i])):
        if K[i][j]==0:
            D[i]=0
            q.append(i)
while q:
    x=q.popleft()
    for nx in S[x]:
        if D[nx]>D[x]+1:
            D[nx]=D[x]+1
            q.append(nx)
k=int(input())
ans=float('inf')
for i in range(1,n+1):
    for j in range(len(K[i])):
        if K[i][j]==k:
            ans=min(ans,D[i])
print(-1 if ans==float('inf') else ans)