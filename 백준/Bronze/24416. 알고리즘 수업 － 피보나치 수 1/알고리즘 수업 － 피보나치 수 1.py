import sys
input=sys.stdin.readline

n=int(input())

def fib(n):
  f1,f2=1,1
  for _ in range(3, n+1):
    f1,f2=f2,f1+f2
  return f2

def fibonacci(n):
    return n-2

print(fib(n), fibonacci(n), sep=' ')