'''
Задача: заменить все пробелы в строке на %20 "на месте"
'''

def get_count_space(string: list) -> int:
    return sum(1 for sym in string if sym == ' ')


def replce_count_symbols(sym: str, string: list, count) -> str:
    i = len(string) - 2 * count - 1
    j = len(string) - 1

    while i >= 0:
        if string[i] == sym:
            string[j] = '0'
            string[j - 1] = '2'
            string[j - 2] = '%'
            j -= 3
        else:
            string[j] = string[i]
            j -= 1
        i -= 1
    return ''.join(string)


string = 'How many people are right?'
string = list(string)
count = get_count_space(string)
string.extend(' ' * 2 * count)
print(replce_count_symbols(' ', string, count))
