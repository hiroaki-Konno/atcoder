def solve():
  N,X=map(int,input().split())
  if N==0 and X==0:
    return False
  P=0
  for i in range(1,N+1):
    for j in range(i+1,N+1):
      for k in range(j+1,N+1):
        if i+j+k==X:
          P+=1
  print(P)
  return True

while solve():
  None
