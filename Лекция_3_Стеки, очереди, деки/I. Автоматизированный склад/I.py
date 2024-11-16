n = int(input())

a, b = map(int, input().split())

cd = {1, 2, 3, 4}
cd.remove(a)
cd.remove(b)
c = cd.pop()
d = cd.pop()
if a > b:
    a, b = b, a
if c > d:
    c, d = d, c

# print(a, b)
# print(c, d)

if (a + b) % 2 == 0:
    line = True
else:
    line = False

rovers = []
for i in range(n):
    dest, t = map(int, input().split())
    rovers.append((dest, t, i + 1))

# print(rovers)
rovers.sort(key=lambda x: (-x[1], -x[2]))
# print(rovers)
st = [[], [], [], []]   # 1, 2, 3, 4

for i in range(n):
    st[rovers[i][0] - 1].append((rovers[i][1], rovers[i][2]))

# print(rovers, line)
# print(st[0], st[1], st[2], st[3])

rovers_res = {}

if line:
    count_time = 1
    while any(st):
        # print('st: ', st)
        if st[a - 1] and st[a - 1][-1][0] <= count_time or st[b - 1] and st[b - 1][-1][0] <= count_time:
            if st[a - 1] and st[a - 1][-1][0] <= count_time:
                rovers_res[st[a - 1][-1][1]] = count_time
                st[a - 1].pop()
            if st[b - 1] and st[b - 1][-1][0] <= count_time:
                rovers_res[st[b - 1][-1][1]] = count_time
                st[b - 1].pop()
        else:
            # print(st[c-1], count_time)
            if st[c - 1] and st[c - 1][-1][0] <= count_time:
                # print('before:')
                # print(st[c - 1])
                rovers_res[st[c - 1][-1][1]] = count_time
                st[c - 1].pop()
                # print('after')
                # print(st[c - 1])
            if st[d - 1] and st[d - 1][-1][0] <= count_time:
                # print(st[d - 1], st[d - 1][-1][0], d, c)
                # print('kek')
                rovers_res[st[d - 1][-1][1]] = count_time
                st[d - 1].pop()
        count_time += 1
else:
    if b == 4 and a == 1:
        a, b = b, a
    elif d == 4 and c == 1:
        c, d = d, c
    count_time = 1
    while any(st):
        if st[a - 1] and st[a - 1][-1][0] <= count_time:
            rovers_res[st[a - 1][-1][1]] = count_time
            st[a - 1].pop()
            count_time += 1
            continue
        elif st[b - 1] and st[b - 1][-1][0] <= count_time:
            rovers_res[st[b - 1][-1][1]] = count_time
            st[b - 1].pop()
            count_time += 1
            continue
        elif st[c - 1] and st[c - 1][-1][0] <= count_time:
            rovers_res[st[c - 1][-1][1]] = count_time
            st[c - 1].pop()
            count_time += 1
            continue
        elif st[d - 1] and st[d - 1][-1][0] <= count_time:
            rovers_res[st[d - 1][-1][1]] = count_time
            st[d - 1].pop()
            count_time += 1
            continue
        else:
            count_time += 1


for i in range(n):
    print(rovers_res[i + 1])

