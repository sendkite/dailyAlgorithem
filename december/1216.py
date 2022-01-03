# 백준 2588 곱셈
A = int(input())
B = input()

line3 = A * int(B[2])
line4 = A * int(B[1])
line5 = A * int(B[0])
res = A * int(B)

print(line3, line4, line5, res)
