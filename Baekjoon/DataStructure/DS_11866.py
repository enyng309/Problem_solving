# 요세푸스 문제 0
from collections import deque
from sys import stdin

N, K = map(int, stdin.readline().split())

queue = deque()
result = []

for i in range(1, N+1):
  queue.append(i)

while queue:
  for i in range(K-1):
    queue.append(queue.popleft())
  result.append(queue.popleft())

print('<', end='')
for i in range(len(result) - 1):
  print('{}, '.format(result[i]), end='')
print('{}>'.format(result[-1]))