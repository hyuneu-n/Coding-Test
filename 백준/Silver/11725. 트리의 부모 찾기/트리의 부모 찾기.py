import sys
from collections import deque

input=sys.stdin.readline

N=int(input())
T=[[] for _ in range(N+1)]
P=[0 for _ in range(N+1)]

for _ in range(N-1):
  a,b=map(int, input().split())
  T[a].append(b)
  T[b].append(a)

def bfs():
  q=deque([1])
  while q:
    node=q.popleft()
    for i in T[node]:
      if P[i]==0:
        P[i]=node
        q.append(i)
  return P

bfs()

for i in P[2:]:
  print(i)