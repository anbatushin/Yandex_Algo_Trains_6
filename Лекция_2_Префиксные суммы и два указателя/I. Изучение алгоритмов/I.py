n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
p = list(map(int, input().split()))

interest = sorted([(a[i], b[i], i) for i in range(n)], key=lambda x: (-x[0], -x[1], x[2]))
useful = sorted([(a[i], b[i], i) for i in range(n)], key=lambda x: (-x[1], -x[0], x[2]))
seen = set()

ind_int = 0
ind_use = 0

# print(interest)
# print(useful)

for i in range(n):
    if p[i] == 0:
        while interest[ind_int] in seen and ind_int < n:
            ind_int += 1
        pair = interest[ind_int]
        print(pair[2] + 1, end=' ')
        seen.add(pair)
        ind_int += 1
    else:
        while useful[ind_use] in seen and ind_use < n:
            ind_use += 1
        pair = useful[ind_use]
        print(pair[2] + 1, end=' ')
        seen.add(pair)
        ind_use += 1
