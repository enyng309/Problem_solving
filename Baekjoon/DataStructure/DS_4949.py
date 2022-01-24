from sys import stdin

ps = {'(': ')', '[': ']'}


while 1:
  T = stdin.readline()
  match = []
  no = False
  
  if T == '.\n':
    break

  for i in range(len(T)):
    if T[i] in '([':
      match.append(T[i])

    elif T[i] in ')]':
      if (not match) or T[i] != ps[match[-1]]:
        no = True
        break
      elif T[i] == ps[match[-1]]:
        #no = False
        match.pop()
    
  if match:
    no = True

  if no == True:
    print('no')
  else:
    print('yes')