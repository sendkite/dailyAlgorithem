# 문자열 검색
import sys

num = int(sys.stdin.readline().rstrip()) # 입력 받을 개수 입력
search = sys.stdin.readline().rstrip() # 검색 단어 입력

words = []
for i in range(num):
    words.append(sys.stdin.readline().rstrip())

result = []
for i in words:
    if i.find(search):
        result.append(i)
print(result)


