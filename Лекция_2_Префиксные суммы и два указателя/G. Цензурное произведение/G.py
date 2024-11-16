n, c = map(int, input().split())
s = input()

max_length = 0

left = 0
right = 0
count_b = 0
count_a = 0
sum = 0
while right < n:
    if s[right] == 'b':
        count_b += 1
        sum += count_a
    if s[right] == 'a':
        count_a += 1

    while sum > c:
        if s[left] == 'a':
            count_a -= 1
            sum -= count_b
        if s[left] == 'b':
            count_b -= 1
        left += 1

    max_length = max(max_length, right - left + 1)
    right += 1

print(max_length)
