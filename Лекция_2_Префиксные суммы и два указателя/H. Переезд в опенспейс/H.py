n = int(input())
a = list(map(int, input().split()))

pref = [0] * (n + 2)
pref_sec = [0] * (n + 2)
suff = [0] * (n + 2)
suff_sec = [0] * (n + 2)

for i in range(n):
    pref[i + 1] += pref[i] + a[i]
    pref_sec[i + 1] += pref_sec[i] + pref[i]
for i in range(n):
    suff[n - i] += suff[n - i + 1] + a[n - i - 1]
    suff_sec[n - i] += suff_sec[n - i + 1] + suff[n - i + 1]

# print(pref) # 5 2 3 1 -> 0 5 5+(5+2)=12 5+5+2+5+2+3=22
# print(pref_sec)            # 5 7 10 11 and 0 5 12 22
# print(suff)
# print(suff_sec)

elem = -1
for i in range(n):
    if elem == -1:
        elem = pref_sec[i + 1] + suff_sec[i + 1]
    else:
        elem = min(elem, pref_sec[i + 1] + suff_sec[i + 1])
print(elem)
