x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x1 < x < x2:
    if abs(y - y1) < abs(y - y2):
        print('S')
    else:
        print('N')
elif y1 < y < y2:
    if abs(x - x1) < abs(x - x2):
        print('W')
    else:
        print('E')
else:
    NW = ((x - x1) ** 2 + (y - y2) ** 2) ** (1 / 2)
    NE = ((x - x2) ** 2 + (y - y2) ** 2) ** (1 / 2)
    SE = ((x - x2) ** 2 + (y - y1) ** 2) ** (1 / 2)
    SW = ((x - x1) ** 2 + (y - y1) ** 2) ** (1 / 2)
    r = min(NW, NE, SE, SW)
    if r == NW:
        print('NW')
    elif r == NE:
        print('NE')
    elif r == SE:
        print('SE')
    else:
        print('SW')
