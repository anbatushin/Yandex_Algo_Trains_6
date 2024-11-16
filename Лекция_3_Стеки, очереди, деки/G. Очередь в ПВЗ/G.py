n, b = map(int, input().split())

a = list(map(int, input().split()))
sum = 0
count = 0

for i in range(n):
    count += a[i]
    sum += count
    count -= b
    if count < 0:
        count = 0

if count > 0:
    sum += count

print(sum)
