n, r = map(int, input().split())
d = list(map(int, input().split()))

count = 0
left = 0
right = 1

while left < right:
    # print(left, right)
    while right < n and d[right] - d[left] <= r:
        right += 1
    # print(left, right, 'lol')
    if right < n:
        # print('count_before = ', count)
        count += n - right
        # print('count_after = ', count)
        left += 1
        if left == right:
            right += 1
    else:
        left = right

print(count)
# 6, 2: 1 1 1 1 6 9 -> 9
