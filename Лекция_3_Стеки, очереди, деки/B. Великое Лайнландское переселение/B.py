n = int(input())
arr = list(map(int, input().split()))

st = []
res = [-1] * n
for i in range(n - 1, -1, -1):
    while st and arr[i] <= arr[st[-1]]:
        st.pop()
    if st:
        res[i] = st[-1]
    st.append(i)

print(*res)
