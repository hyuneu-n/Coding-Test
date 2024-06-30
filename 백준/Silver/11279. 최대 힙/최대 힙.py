import heapq
import sys
N=int(input())
num=0
arr=[]
for i in range(N):
    num=int(sys.stdin.readline())
    if num==0:
        if len(arr)==0:print(0)
        else:
            print(-arr[0])
            heapq.heappop(arr)
    else:
        heapq.heappush(arr,-num)