'''
Нужно реализовать функцию OneEditApart, проверяющую, можно ли получить одну строку из другой,
не более чем за одно исправление (удаление, доьавление, изменение символа).
Например:
OneEditApart("cat", "dog") -> false
OneEditApart("cat", "cats") -> true
OneEditApart("cat", "cut") -> true
OneEditApart("cat", "cast") -> true
OneEditApart("cat", "at") -> true
OneEditApart("cat", "acts") -> false
'''

def OneEditApart(first: str, second: str) -> bool:
    if abs(len(first) - len(second)) > 1:
        return False

    is_diff = False
    if len(first) == len(second):
        for i in range(len(first)):
            if first[i] != second[i]:
                if is_diff:
                    return False
                is_diff = True
    else:
        if len(first) < len(second):
            first, second = second, first

        i = 0
        while i < len(second):
            if is_diff:
                if first[i + 1] != second[i]:
                    return False
            elif first[i] != second[i]:
                is_diff = True
                continue
            i += 1
    return True


print(OneEditApart("cat", "dog"))
print(OneEditApart("cat", "cats"))
print(OneEditApart("cat", "cut"))
print(OneEditApart("cat", "cast"))
print(OneEditApart("cat", "at"))
print(OneEditApart("cat", "acts"))
