# 쇠막대기
barNlaser = list(input())
bar = 0
stack = []

for i in range(len(barNlaser)):
  if barNlaser[i] == '(':
    stack.append('(')
  else:
    if barNlaser[i - 1] == '(':
      stack.pop()
      bar += len(stack)
    else:
      stack.pop()
      bar += 1
print(bar)
