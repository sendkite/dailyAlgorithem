import sys


checker = sys.stdin.readline().rstrip()
result = []
count = {}

for i in checker:
    if i not in result:
        cnt = 0
        result.append(i)
        result.append(str(cnt))
# 참조를 어떻게...?
print(result)

