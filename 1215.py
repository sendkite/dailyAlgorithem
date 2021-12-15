# 백준 2884 알림시계
H, M = map(int, input().split())

if 0 <= H <= 23 and 0 <= M <= 59:
    if M - 45 < 0:
        if H == 0:
            H = 23
        else:
            H = H - 1
        M = M - 45
        print(H, 60 + M)
    else:
        print(H, M - 45)

