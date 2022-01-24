K = int(input())

list_num = []

for _ in range(K):
  num = int(input())
  if num == 0:
    list_num.pop()
  else:
    list_num.append(num)

result = sum(list_num)
print(result)
