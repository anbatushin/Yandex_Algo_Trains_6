n, k = map(int, input().split())

mas = list(map(int, input().split()))

mas_1 = [0] * n
mas_2 = [0] * n

for i in range(n):
    if i % k:
        mas_1[i] = min(mas[i], mas_1[i - 1])
    else:
        mas_1[i] = mas[i]

mas_2[n - 1] = mas[n - 1]
for i in range(n - 2, -1, -1):
    if (i + 1) % k:
        mas_2[i] = min(mas[i], mas_2[i + 1])
    else:
        mas_2[i] = mas[i]

for i in range(n - k + 1):
    print(min(mas_2[i], mas_1[i + k - 1]))
