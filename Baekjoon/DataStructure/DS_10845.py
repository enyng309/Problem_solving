from sys import stdin

N = int(stdin.readline())
q = []

for _ in range(N):
  indic_num = stdin.readline().split()

  if indic_num[0] == "push":
    q.append(indic_num[1])
  
  elif indic_num[0] == "pop":
    if q:
      print(q.pop(0))
    else:
      print(-1)
  
  elif indic_num[0] == "size":
    print(len(q))
  
  elif indic_num[0] == "empty":
    if q:
      print(0)
    else:
      print(1)

  elif indic_num[0] == "front":
    if not q:
      print(-1)
    else:
      print(q[0])
  elif indic_num[0] == "back":
    if not q:
      print(-1)
    else:
      print(q[-1])