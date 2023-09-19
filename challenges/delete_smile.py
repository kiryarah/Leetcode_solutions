'''
Удалить смайлы, вида :-)+ и :-(+
'''

def del_current_seq(string, sym, right):

    left = right

    while right < len(string) - 2 and string[right + 2] == sym:
        right += 1

    string[left: right + 2] = ''

    return right


def delete_smile(string: str) -> str:
    string = list(string)
    i = 0

    while i < len(string) - 1:

        while i < len(string) - 1 and (string[i] != ':' or string[i + 1] != '-'):
            i += 1

        if i < len(string) - 2 and string[i + 2] == ')':
            i = del_current_seq(string, ')', i)

        if i < len(string) - 2 and string[i + 2] == '(':
            i = del_current_seq(string, '(', i)

        i += 1

    return ''.join(string)


string = 'Я работаю в гугле_:-)))'
print(delete_smile(string))
string = 'везет :-) а я туда собеседование завалил:-(('
print(delete_smile(string))
string = 'лол:-) ))))_:-((('
print(delete_smile(string))
string = 'Ааааа!!!!! :-))(())'
print(delete_smile(string))



'''
    Используя регулярные выражения~
'''

from re import sub


def remove_smiles(string):
    return sub(r':-\)+|:-\(+', '', string)


string = '''
Я работаю в Гугле :-))))
Везет. А я тогда собос завалил:-((((
Лол:)
Aaaaaaaaa!!!!!!!! :-))(())
'''

print(remove_smiles(string))
