# 선택 정렬

input = [4, 6, 2, 9, 1]


def selection_sort(array):
    result = []
    for i in range(len(array)):
        result.append(min(array))
        array.remove(min(array))
    return print(result)

selection_sort(input)
print(input)

