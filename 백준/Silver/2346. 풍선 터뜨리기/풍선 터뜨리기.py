import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
deq=deque(list(enumerate(map(int, input().split()))))
num=[]

while deq:
    idx,number=deq.popleft()
    num.append(idx+1)

    if number>0:
        deq.rotate(-(number-1))
    elif number<0:
        deq.rotate(-number)

print(' '.join(map(str,num)))