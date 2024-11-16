n = int(input())
a = list(map(int, input().split()))

a.sort()

if len(a) % 2 == 0:
    index = len(a) // 2 - 1
    k = 1
else:
    index = len(a) // 2
    k = -1

# print(a)
# print(index)
while -1 < index < n:
    # print(index, k)
    print(a[index], end=' ')
    index += k
    if k < 0:
        k -= 1
    else:
        k += 1
    k *= -1

# 1 2 3 4 5 -> 3 (1245), 2 (145), 4 (15), 1(5), 5
