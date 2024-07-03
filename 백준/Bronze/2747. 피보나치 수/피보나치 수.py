n=int(input())

for i in range(n):
  f1,f2=1,1
  for _ in range(3, n+1):
    f1,f2=f2,f1+f2

print(f2)