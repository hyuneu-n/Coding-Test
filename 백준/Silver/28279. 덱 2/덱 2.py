import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
dec=deque()

for _ in range(N):
    cmd=input().split()

    if cmd[0]=='1':
        dec.insert(0,cmd[1])
    elif cmd[0]=='2':
        dec.append(cmd[1])
    elif cmd[0]=='3':
        if dec:
            print(dec.popleft())
        else:
            print(-1)
    elif cmd[0]=='4':
        if dec:
            print(dec.pop())
        else:
            print(-1)
    elif cmd[0]=='5':
        print(len(dec))
    elif cmd[0]=='6':
        if dec:
            print(0)
        else:
            print(1)
    elif cmd[0]=='7':
        if dec:
            print(dec[0])
        else:
            print(-1)
    elif cmd[0]=='8':
        if dec:
            print(dec[len(dec)-1])
        else:
            print(-1)