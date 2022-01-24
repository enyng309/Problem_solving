K = int(input())

stack = []
result = []
start = 1
no = False

for _ in range(K):
  num = int(input())

  while start <= num:
    stack.append(start)
    result.append("+")
    start += 1

  if stack[-1] == num:
    stack.pop()
    result.append("-")
  else:
    print("NO")
    no = True
    break

if no == False:
  for i in result:
    print(i)