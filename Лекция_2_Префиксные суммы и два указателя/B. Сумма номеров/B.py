N, K = map(int, input().split())
a = list(map(int, input().split()))

L = 0
sum = 0
count = 0

for R in range(N):
    sum += a[R]

    while sum > K and L <= R:
        sum -= a[L]
        L += 1

    if sum == K:
        count += 1
        tmp = sum
        tmp_l = L
        while tmp_l < R and tmp == K:
            tmp -= a[tmp_l]
            tmp_l += 1
            if tmp == K:
                count += 1

print(count)
