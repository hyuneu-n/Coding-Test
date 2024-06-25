import sys

n=int(sys.stdin.readline())
lst=[]

for i in range(n):
    x,y=map(int, input().split())
    lst.append([x,y])

s_lst=sorted(lst)

for x,y in s_lst:
    print(x,y)