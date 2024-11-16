from collections import deque

n, H = map(int, input().split())
h = list(map(int, input().split()))
w = list(map(int, input().split()))

chairs = [(h[i], w[i]) for i in range(n)]
chairs.sort(key=lambda x: x[0])

left, right = 0, 0
sum_w = 0
min_h_delta = float('inf')
delta_deque = deque()

while right < n:
    sum_w += chairs[right][1]

    if right > left:
        delta = chairs[right][0] - chairs[right - 1][0]
        while delta_deque and delta_deque[-1] < delta:
            delta_deque.pop()
        delta_deque.append(delta)

    while sum_w >= H:
        h_delta = delta_deque[0] if delta_deque else 0
        min_h_delta = min(min_h_delta, h_delta)
        sum_w -= chairs[left][1]

        if delta_deque and left < right:
            if delta_deque[0] == chairs[left + 1][0] - chairs[left][0]:
                delta_deque.popleft()

        left += 1

    right += 1

print(min_h_delta)
