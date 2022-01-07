# 문자열 조작하기
# 문자열 -> 리스트 == list(문자열)
# 리스트 -> 문자열 == "".join(리스트)
# 딕셔너리 값 가져오기 == 딕셔너리.get(키)
import sys

name = list(sys.stdin.readline().rstrip())
print(name)
checker = {
    "A": "4",
    "E": "3",
    "G": "6",
    "I": "1",
    "O": "0",
    "S": "5",
    "Z": "2"
}

result = []
for i in name:
    if i in checker:
        result.append(checker.get(i))
    else:
        result.append(i)
print("".join(result))
