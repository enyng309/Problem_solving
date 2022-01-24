from sys import stdin

T = int(stdin.readline())

for _ in range(T):
  ps = stdin.readline().strip()
  vps = 0

  for i in range(len(ps)):
    if ps[i] == '(':
      vps += 1
    elif ps[i] == ')':
      vps -= 1

    if vps < 0:
      print('NO')
      break

  if vps == 0:
    print('YES')
  elif vps > 0:
    print('NO')