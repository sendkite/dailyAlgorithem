# 순차적 문자열 변환

import sys

name = sys.stdin.readline().rstrip()

cnt = len(name)
for i in range(cnt):
    name = name.replace(name[cnt - 1], '#')
    cnt = cnt - 1
    print(name)
    if cnt == 0:
        break

