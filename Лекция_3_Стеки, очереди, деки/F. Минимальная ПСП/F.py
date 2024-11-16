def construct(n, w, s):
    priority = {}
    for i in range(4):
        priority[w[i]] = i

    st = []
    s2 = []
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            st.append('(')
            count += 1
        elif s[i] == '[':
            st.append('[')
            count += 1
        elif s[i] == ')':
            st.pop()
            count -= 1
        elif s[i] == ']':
            st.pop()
            count -= 1

        s2.append(s[i])

    for i in range(len(s), n):
        if count + 1 > (n - i):
            more = False
            # print(count, s2, n, i)
        else:
            more = True

        if more:
            if priority['('] < priority['[']:
                c = '('
            else:
                c = '['

            if st and st[-1] == '(':
                if priority[')'] < priority[c]:
                    # print('lol', s2)
                    s2.append(')')
                    st.pop()
                    count -= 1
                else:
                    s2.append(c)
                    st.append(c)
                    count += 1
            elif st and st[-1] == '[':
                if priority[']'] < priority[c]:
                    s2.append(']')
                    st.pop()
                    count -= 1
                else:
                    s2.append(c)
                    st.append(c)
                    count += 1
            else:
                s2.append(c)
                st.append(c)
                count += 1

        else:
            if st[-1] == '(':
                s2.append(')')
                st.pop()
                count -= 1
            else:
                s2.append(']')
                st.pop()
                count -= 1

    print(''.join(s2))


n = int(input())
w = input()
s = list(input())
# print(s)

construct(n, w, s)
