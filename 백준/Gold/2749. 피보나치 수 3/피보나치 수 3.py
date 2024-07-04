n = int(input()) % (15 * 10**5)

f = [0] * (n+1)
f[0] = 0
f[1] = 1
for i in range(2,n+1):
    f[i] = (f[i-2] + f[i-1]) % 1000000
print(f[n])
#피사노주기;;