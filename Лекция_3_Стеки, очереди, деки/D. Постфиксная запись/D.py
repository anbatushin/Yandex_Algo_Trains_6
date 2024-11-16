s = input().split()

st = []
for char in s:
    if char == '+':
        st.append(st.pop() + st.pop())
    elif char == '-':
        a, b = st.pop(), st.pop()
        st.append(b - a)
    elif char == '*':
        st.append(st.pop() * st.pop())
    else:
        st.append(int(char))

res = st.pop()
print(res)
