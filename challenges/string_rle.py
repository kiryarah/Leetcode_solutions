'''
Дана строка, состоящая из букв A-Z:
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно вернуть:
A4B3C2XYZD4E3F3A6B28
И сгенерировать исключение, если на вход пришла невалидная строка.
'''

def is_valid(sym: str):
    if not(ord(sym) in range(ord('A'), ord('Z') + 1)):
        raise TypeError('Введена не валидная строка!')


def get_rle(string: str):
    result = []
    i, j = 0, 1
    is_valid(string[0])

    while j < len(string):
        is_valid(string[j])
        if string[j] != string[j - 1] or j == len(string) - 1:
            count = j - i if j < len(string) - 1 else j - i + 1
            result.append(f'{string[i]}{count if count > 1 else ""}')
            i = j
        j += 1
    return ''.join(result)


print(get_rle('AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
