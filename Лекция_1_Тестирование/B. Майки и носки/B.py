A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A == 0 or B == 0:
    M = 1
    if A == 0:
        N = C + 1
    elif B == 0:
        N = D + 1
    print(M, N)
elif C == 0 or D == 0:
    N = 1
    if C == 0:
        M = A + 1
    elif D == 0:
        M = B + 1
    print(M, N)
else:
    if A == B and C == D:
        if A > C:
            print(1, C + 1)
        else:
            print(A + 1, 1)
    elif A == B:
        print(A + 1, 1)
    elif C == D:
        print(1, C + 1)
    else:
        M1 = A + 1
        N1 = C + 1
        M2 = B + 1
        N2 = D + 1
        '''
        if M1 + N1 < M2 + N2:
            if M1 + N1 < min(A, B) + min(C, D) + 2:
                print(M1, N1)
            else:
                print(min(A, B) + 1, min(C, D) + 1)
        else:
            if M2 + N2 < min(A, B) + min(C, D) + 2:
                print(M2, N2)
            else:
                print(min(A, B) + 1, min(C, D) + 1)
        '''
        if max(A, B) < max(C, D):
            M3 = max(A, B) + 1
            N3 = 1
        else:
            M3 = 1
            N3 = max(C, D) + 1
        if M1 + N1 < M2 + N2:
            if M1 + N1 < M3 + N3:
                print(M1, N1)
            else:
                print(M3, N3)
        else:
            if M2 + N2 < M3 + N3:
                print(M2, N2)
            else:
                print(M3, N3)
