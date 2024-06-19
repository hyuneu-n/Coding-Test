import sys

n=int(sys.stdin.readline())
lst=[]

for i in range(n):
    x,y=map(int, input().split())
    lst.append([y,x])

s_lst=sorted(lst)

for y,x in s_lst:
    print(x,y)