def get_coords(matrix, x1, y1, x2, y2, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '#':
                x1 = min(x1, j)
                y1 = max(y1, i)
                x2 = max(x2, j)
                y2 = min(y2, i)

    return x1, y1, x2, y2


def check_lights(matrix, x1, y1, x2, y2):
    x3, y3 = -1, -1
    x4, y4 = -1, -1
    x5, y5 = -1, -1
    x6, y6 = -1, -1
    errfl = False
    fuckitimdone = True
    for i in range(y2, y1):
        for j in range(x1, x2):
            if not errfl and matrix[i][j] == '.':
                fuckitimdone = False
                if y5 == -1 and (y3 != -1 and i > y3 or y3 == -1):
                    # print('count', i, j)
                    k = i
                    while k < y1 and matrix[k][j] == '.':
                        k += 1
                    if x3 == -1:
                        x3 = j
                        y3 = k
                    elif x5 == -1:
                        x5 = j
                        y5 = k
                    else:
                        errfl = True

                    k = j
                    while k < x2 and matrix[i][k] == '.':
                        k += 1
                    if x4 == -1:
                        x4 = k
                        y4 = i
                    elif x6 == -1:
                        x6 = k
                        y6 = i
                    else:
                        errfl = True
                elif y4 <= i <= y3 and x3 <= j <= x4 or y6 <= i <= y5 and x5 <= j <= x6:
                    continue
                else:
                    errfl = True
                    # print('lol', i, j, y4, i, y3, x4, j, x3)
            elif not errfl and (y4 <= i < y3 and x3 <= j < x4 or y6 <= i < y5 and x5 <= j < x6):
                errfl = True
                # print('gayporno')
                # print(i, j)

    if errfl:
        print('X')
    elif fuckitimdone:
        print('I')
    elif x5 == -1:  # -> O, C, L
        if x1 < x3 < x4 < x2 and y2 < y4 < y3 < y1:
            print('O')
        elif x1 < x3 < x4 == x2 and y2 < y4 < y3 < y1:
            print('C')
        elif x1 < x3 < x4 == x2 and y2 == y4 < y3 < y1:
            print('L')
        else:
            print('X')
    elif x1 < x3 == x5 < x4 == x6 < x2 and y2 == y4 < y3 < y6 < y5 == y1:
        print('H')
    elif x1 < x3 == x5 < x4 < x6 == x2 and y2 < y4 < y3 < y6 < y5 == y1:
        print('P')
    else:
        print('X')

    return


n = int(input())
matrix = [input().strip() for _ in range(n)]

x1, y1 = n + 1, -1
x2, y2 = -1, n + 1

x1, y1, x2, y2 = get_coords(matrix, x1, y1, x2, y2, n)
if x1 > x2 or y2 > y1:
    print('X')
else:
    # print(x1, y1+1, x2+1, y2, [matrix[i][j] for i in range(y2, y1 + 1) for j in range(x1, x2 + 1)])
    check_lights(matrix, x1, y1 + 1, x2 + 1, y2)
