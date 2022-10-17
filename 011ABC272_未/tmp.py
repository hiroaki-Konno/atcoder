from collections import deque

N,M=map(int,input().split())

able=[]
for i in range(M+1):
  n=M-i**2
  if n<0:
    break
  n=n**0.5
  if int(n)==n:
    n=int(n)
    able.append([i,n])
    able.append([i,-n])
    able.append([-i,n])
    able.append([-i,-n])

D=deque(); D.append([0,0])
dist=[[-1]*N for _ in range(N)]; dist[0][0]=0
ok=lambda x,y:0<=x<N and 0<=y<N and dist[x][y]==-1
while D:
  x,y=D.popleft()
  for a,b in able:
    nx,ny=x+a,y+b
    if not ok(nx,ny):
      continue
    dist[nx][ny]=dist[x][y]+1
    D.append([nx,ny])

for n in dist:
  print(*n,sep=" ")