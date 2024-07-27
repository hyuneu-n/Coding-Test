import sys
input=sys.stdin.readline

N = int(input().strip())
N_s = list(map(int, input().strip().split()))
M = int(input().strip())
M_s = list(map(int, input().strip().split()))

n_dic = {}

for n in N_s:
  if n in n_dic:
    n_dic[n] += 1
  else:
    n_dic[n] = 1

for m in M_s:
  if m in n_dic:
    print(n_dic[m], end=' ')
  else:
     print(0, end=' ')