n = int(input())
a = list(map(int, input().split()))

b = [0] * (n + 1)

for i in range(n):
    print(b[i] + a[i], end=' ')
    b[i + 1] += b[i] + a[i]
