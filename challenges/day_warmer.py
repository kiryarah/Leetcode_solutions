'''
Задача: Дан массив чисел. Каждый из которых представляет дневную температуру.
Для каждой температуры необходимо узнать: сколько суток должно пройти, чтобы наступил более теплый день.
Например: [11, 15, 12, 20]
Вывод: [1, 2, 1, 0]

'''

def get_warmer_days(tems: list) -> list:
    stack = []

    for i in range(len(tems) - 1, -1, -1):
        while stack and stack[-1][0] <= tems[i]:
            stack.pop()

        middle = stack[-1][1] - i if stack else 0
        stack.append((tems[i], i))
        tems[i] = middle
    return tems


print(get_warmer_days([11, 15, 12, 20]))
