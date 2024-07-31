a = int(input())
b = list(map(int, input().split()))
c = list(map(int, input().split()))
print(len(b)*c[0]//100, end=' ')
n = 0
for i in range(len(b)):
    if b[i] >= c[1]:
        n += 1
print(n)