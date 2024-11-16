def parser(s):
    def check_pars(c):
        if c.isdigit():
            return 'digit'
        elif c in '()':
            return '()'
        return 'ops'

    step = check_pars(s[0])
    if len(s) > 1:
        space_fl = False
        for i in range(1, len(s)):
            if s[i] == ' ':
                space_fl = True
            else:
                tmp_step = check_pars(s[i])
                if space_fl:
                    space_fl = False
                    if step == tmp_step and step != '()':
                        # print('lol', step, tmp_step, s[i])
                        print('WRONG')
                        return False
                step = tmp_step
    return True


def calculate(s):
    def check(s):
        count = 0
        for ch in s:
            if ch not in '0123456789-+*()':
                return False
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False
        if count != 0:
            return False
        return True

    def sum_dec_mult(nums, st):
        a = nums.pop()
        if not nums:
            st.pop()
            return
        b = nums.pop()
        op = st.pop()
        if op == '+':
            nums.append(a + b)
        elif op == '-':
            nums.append(b - a)
        elif op == '*':
            nums.append(a * b)
        return

    def priority(op):
        if op == '+' or op == '-':
            return 1
        elif op == '*':
            return 2
        return 0

    nums = []
    st = []

    if not check(s):
        # print('lol')
        print('WRONG')
        return

    index = 0
    while index < len(s):
        ch = s[index]
        if ch == '(':
            st.append(ch)
        elif ch == ')':
            while st and st[-1] != '(':
                sum_dec_mult(nums, st)
            st.pop()
        elif ch in '-+*':
            while st and st[-1] != '(' and priority(ch) <= priority(st[-1]):
                sum_dec_mult(nums, st)
            st.append(ch)
        else:
            num = 0
            while index < len(s) and s[index].isdigit():
                num = num * 10 + int(s[index])
                index += 1
            nums.append(num)
            index -= 1
        # print(nums, st)

        index += 1

    while st and nums:
        sum_dec_mult(nums, st)

    # print(st, nums)
    if nums:
        print(nums[0])
    else:
        # print('lol')
        print('WRONG')

    return


s = input()
if parser(s):
    calculate(s.replace(' ', ''))
