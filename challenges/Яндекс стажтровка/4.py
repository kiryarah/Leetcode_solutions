class Country:
    def __init__(self, index, profit, education=0, nationality=0) -> None:
        self.index = index
        self.profit = profit
        self.education = education
        self.nationality = nationality

    def __str__(self) -> str:
        return f'{self.index}: {self.profit}, {self.education}, {self.nationality}'


class Classmate:
    def __init__(self, profit, education=0, nationality=0) -> None:
        self.profit = profit
        self.education = education
        self.nationality = nationality

    def __str__(self) -> str:
        return f'Classmate: {self.profit}, {self.education}, {self.nationality}'

    def __repr__(self) -> str:
        return f'Classmate: {self.profit}, {self.education}, {self.nationality}'


def binary_search(array, search_num):
    mid = len(array) // 2
    left, right = 0, len(array) - 1

    while left <= right:
        if array[mid].profit == search_num:
            return array[mid].index

        if search_num < array[mid].profit:
            right = mid - 1
        else:
            left = mid + 1
        mid = (left + right) // 2
    return array[mid].index


n = int(input())
cntrs = [Country(i, int(profit)) for i, profit in enumerate(input().split())]

for i, edu in enumerate(input().split()):
    cntrs[i].education = int(edu)

for i, nation in enumerate(input().split()):
    cntrs[i].nationality = int(nation)

q = int(input())
clsmts = [Classmate(int(profit)) for profit in input().split()]

for i, edu in enumerate(input().split()):
    clsmts[i].education = int(edu)

for i, nation in enumerate(input().split()):
    clsmts[i].nationality = int(nation)

cntrs_edu = list(filter(lambda x: x.education == 1, cntrs))
cntrs_edu.append(Country(n, float('-inf'), 1))
cntrs_not_edu = list(filter(lambda x: x.education == 0, cntrs))
cntrs_not_edu.append(Country(n, float('-inf'), 0))

cntrs_edu.sort(key=lambda x: x.profit)
cntrs_not_edu.sort(key=lambda x: x.profit)

for i in range(1, len(cntrs_edu)):
    if cntrs_edu[i].index > cntrs_edu[i - 1].index:
        cntrs_edu[i].index = cntrs_edu[i - 1].index

for i in range(1, len(cntrs_not_edu)):
    if cntrs_not_edu[i].index > cntrs_not_edu[i - 1].index:
        cntrs_not_edu[i].index = cntrs_not_edu[i - 1].index

result = []

for classmate in clsmts:
    nation_index = profit_index = n + 1
    if classmate.nationality and cntrs[classmate.nationality - 1].nationality:
        nation_index = classmate.nationality
    if classmate.education == 0:
        profit_index = binary_search(cntrs_not_edu, classmate.profit) + 1
    else:
        profit_index = min(binary_search(
            cntrs_not_edu, classmate.profit), binary_search(cntrs_edu, classmate.profit)) + 1

    res_min_index = min(nation_index, profit_index)
    result.append(res_min_index if res_min_index <= n else 0)

print(*result)
