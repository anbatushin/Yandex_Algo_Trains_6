n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
left = 0
right = 0
max_len = 0
while right < n:
    if a[right] - a[left] > k:
        while left <= right and a[right] - a[left] > k:
            left += 1
    max_len = max(max_len, right - left + 1)
    right += 1

print(max_len)
