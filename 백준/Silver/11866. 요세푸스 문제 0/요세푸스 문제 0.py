N, K = map(int, input().split())

lst = []
arr = [*range(1, N + 1)]
num = 0

for i in range(N):
    num += K - 1
    if num >= len(arr):
        num = num % len(arr)
    
    lst.append(str(arr.pop(num)))

print("<", ", ".join(lst), ">", sep='')