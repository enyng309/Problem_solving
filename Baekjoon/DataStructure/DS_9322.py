from sys import stdin

test_num = int(stdin.readline())

for _ in range(test_num):
  stc_size = int(stdin.readline())
  public1 = stdin.readline().split()
  public2 = stdin.readline().split()
  cryptogram = stdin.readline().split()
  idx = []
  decode = []

  for i in range(stc_size):
    idx.append(public1.index(public2[i]))

  for i in range(stc_size):
    decode.append(cryptogram[idx.index(i)])
    print(decode[i], end=' ')