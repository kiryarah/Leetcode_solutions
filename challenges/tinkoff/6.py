# Structure
class DisjointSetUnion:
    def __init__(self, n) -> None:
        self.__lenght = n + 1
        self.__parent = [0] * self.__lenght
        self.__size = [1] * self.__lenght
        self.__changed_count = [1] * self.__lenght

    def make_set(self, value: int) -> None:
        self.__parent[value] = value

    def find_set(self, value: int) -> int:
        if value == self.__parent[value]:
            return value

        self.__parent[value] = self.find_set(self.__parent[value])
        return self.__parent[value]

    def __update_sets_count(self, root: int) -> None:
        for i in range(self.__lenght):
            if self.__parent[i] == root:
                self.__changed_count[i] += 1

    def union_sets(self, set_x: int, set_y: int) -> None:
        set_x = self.find_set(set_x)
        set_y = self.find_set(set_y)

        if set_x == set_y:
            return

        if self.__size[set_x] < self.__size[set_y]:
            set_x, set_y = set_y, set_x

        self.__parent[set_y] = set_x
        self.__size[set_x] += self.__size[set_y]
        self.__update_sets_count(set_x)

    def __str__(self) -> str:
        return f'{self.__parent}'

    def get_count_team(self, value: int) -> int:
        return self.__changed_count[value]


# Service requests handler
def is_both_sameteam(x: int, y: int, dsu: DisjointSetUnion) -> int:
    return 'YES' if dsu.find_set(x) == dsu.find_set(y) else 'NO'


def union_teams(x: int, y: int, dsu: DisjointSetUnion) -> None:
    dsu.union_sets(x, y)


def get_count_teams(x: int, dsu: DisjointSetUnion) -> int:
    return dsu.get_count_team(x)


# Main
n, m = map(int, input().split())

dsu = DisjointSetUnion(n)

req_dict = {
    1: union_teams,
    2: is_both_sameteam,
    3: get_count_teams,
    }

for i in range(1, n + 1):
    dsu.make_set(i)

result = []

for _ in range(m):
    req_number, *args = map(int, input().split())
    response = req_dict.get(req_number)(*args, dsu)
    if response:
        result.append(response)

print(*result, sep='\n')
