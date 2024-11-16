n = int(input())

sum = [0] * (n + 1)
stack = []
count = 0

for i in range(n):
    s = input()
    if s[0] == '+':
        num = int(s[1:])
        count += 1
        sum[count] = sum[count - 1] + num
        stack.append(num)
    elif s[0] == '-':
        num = stack.pop()
        print(num)
        sum[count] = 0
        count -= 1
    elif s[0] == '?':
        k = int(s[1:])
        print(sum[count] - sum[count - k])
