p = 1000000007
n = int(input())
a = list(map(int, input().split()))

tmp_frst, tmp_sec = 0, 0
res = 0

for i in range(n):
    res = (res + a[n - i - 1] * tmp_sec) % p
    tmp_sec = (tmp_sec + a[n - i - 1] * tmp_frst) % p
    tmp_frst = (tmp_frst + a[n - i - 1]) % p

print(res)
