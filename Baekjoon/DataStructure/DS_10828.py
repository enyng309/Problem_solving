from sys import stdin

N = int(stdin.readline())
stack = []

for _ in range(N):
  indic_num = stdin.readline().split()

  if indic_num[0] == "push":
    stack.append(indic_num[1])
  
  elif indic_num[0] == "pop":
    if stack:
      print(stack.pop())
    else:
      print(-1)
  
  elif indic_num[0] == "size":
    print(len(stack))
  
  elif indic_num[0] == "empty":
    if stack:
      print(0)
    else:
      print(1)

  elif indic_num[0] == "top":
    if not stack:
      print(-1)
    else:
      print(stack[-1])