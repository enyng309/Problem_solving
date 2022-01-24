from sys import stdin

test_num = int(stdin.readline())

for _ in range(test_num):
  n, m = map(int, stdin.readline().split())
  importance = list(map(int, stdin.readline().split()))
  original = list(range(len(importance)))
  original[m] = 'key'

  order = 0
  
  while True:
    if importance[0] == max(importance):
      order += 1

      if original[0] == 'key':
        print(order)
        break

      else:
        importance.pop(0)
        original.pop(0)

    else:
      importance.append(importance.pop(0))
      original.append(original.pop(0))