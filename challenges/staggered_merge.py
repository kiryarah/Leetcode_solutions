'''
Есть 2 ступенчатых графика. Которые представлены массивами данных вида:{время_значения, значения}.
Величины сохраняют свои значения между измерениями. До 1го измерения величина равно 0.
Нужно сформировать массив, который будет содержать сумму 2х представленных массивов.
Пример:
a = {1, 2}, {5, 1}
b = {2, 4}, {3,6}, {9, 7}
result = {1, 2}, {2, 6}, {3, 8}, {5, 7}, {9, 8}
'''

def merge_arrays(a: list, b: list) -> list:
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i][0] <= b[j][0]:
            current = 0 if j == 0 else b[j - 1][1]
            result.append((a[i][0], a[i][1] + current))
            i += 1
        else:
            current = 0 if i == 0 else a[i - 1][1]
            result.append((b[j][0], b[j][1] + current))
            j += 1

    while i < len(a):
        result.append((a[i][0], a[i][1] + b[j - 1][1]))
        i += 1

    while j < len(b):
        result.append((b[j][0], b[j][1] + a[i - 1][1]))
        j += 1

    return result


a = [(1, 2), (5, 1)]
b = [(2, 4), (3, 6), (9, 7)]

print(*merge_arrays(a, b))
