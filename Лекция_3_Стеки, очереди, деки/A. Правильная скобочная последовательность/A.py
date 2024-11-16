s = input()
st = []
fl = True
for c in s:
    if c in '([{':
        st.append(c)
    else:
        if not st:
            fl = False
            break
        if c == ')' and st[-1] == '(':
            st.pop()
        elif c == ']' and st[-1] == '[':
            st.pop()
        elif c == '}' and st[-1] == '{':
            st.pop()
        else:
            fl = False

if not fl or st:
    print('no')
else:
    print('yes')
