import sys
input=sys.stdin.readline

N,K=map(int, input().split())
lst=[]
for _ in range(N):
  lst.append(int(input()))
lst.sort(reverse=True)

ans=0
for S in lst:
  if K>=S:
    ans += K//S
    K%=S
    if K<=0:
      break
print(ans)