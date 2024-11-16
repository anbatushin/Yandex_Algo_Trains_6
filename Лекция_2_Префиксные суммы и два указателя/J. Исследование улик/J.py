n = int(input())
a = list(map(int, input().split()))
m, k = map(int, input().split())
x = list(map(int, input().split()))

pref = [0] * n
count = 0

for i in range(1, n):
    if a[i - 1] < a[i]:
        pref[i] = pref[i - 1]
    elif a[i - 1] == a[i]:
        count += 1
        pref[i] = pref[i - 1]
        while count > k:
            count -= (a[pref[i]] == a[pref[i] + 1])
            # print(count, ' lol ')
            pref[i] += 1
    else:
        pref[i] = i
        count = 0
    # print(pref)
    # print(count)

for xi in x:
    print(pref[xi - 1] + 1, end=' ')
