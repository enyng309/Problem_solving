from sys import stdin

N = int(stdin.readline())
deq = []

for _ in range(N):
  indic_num = stdin.readline().split()

  if indic_num[0] == "push_front":
    deq.insert(0, indic_num[1])

  elif indic_num[0] == "push_back":
    deq.append(indic_num[1])
  
  elif indic_num[0] == "pop_front":
    if deq:
      print(deq.pop(0))
    else:
      print(-1)
  
  elif indic_num[0] == "pop_back":
    if deq:
      print(deq.pop())
    else:
      print(-1)

  elif indic_num[0] == "size":
    print(len(deq))
  
  elif indic_num[0] == "empty":
    if deq:
      print(0)
    else:
      print(1)

  elif indic_num[0] == "front":
    if not deq:
      print(-1)
    else:
      print(deq[0])

  elif indic_num[0] == "back":
    if not deq:
      print(-1)
    else:
      print(deq[-1])