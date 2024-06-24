T=int(input())

ans=[0]*11

ans[1]=1
ans[2]=2
ans[3]=4

for i in range(4,11):
  ans[i]=ans[i-3]+ans[i-2]+ans[i-1]

for _ in range(T):
  n=int(input())
  print(ans[n])