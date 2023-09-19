# Structure
class DisjointSetUnion:
    def __init__(self, n) -> None:
        self.__lenght = n + 1
        self.__parent = [0] * self.__lenght
        self.__size = [1] * self.__lenght
        self.__set_mins = [float('inf')] * self.__lenght

    def make_set(self, value: int) -> None:
        self.__parent[value] = value

    def find_set(self, value: int) -> int:
        if value == self.__parent[value]:
            return value

        self.__parent[value] = self.find_set(self.__parent[value])
        return self.__parent[value]

    def __update_set_mins(self, root: int, w: int) -> None:
        for i in range(self.__lenght):
            if self.__parent[i] == root:
                self.__set_mins[i] = w

    def union_sets(self, set_x: int, set_y: int, w: int) -> None:
        x = self.find_set(set_x)
        y = self.find_set(set_y)

        if x == y:
            if self.__set_mins[x] < w:
                self.__update_set_mins(x, w)
            return

        set_x, set_y = x, y

        if self.__size[set_x] < self.__size[set_y]:
            set_x, set_y = set_y, set_x

        self.__parent[set_y] = set_x

        if self.__set_mins[set_x] > w:
            self.__update_set_mins(set_x, w)

        self.__size[set_x] += self.__size[set_y]

    def __str__(self) -> str:
        return f'{self.__parent}'

    def get_set_mins(self):
        return self.__set_mins


n, m = map(int, input().split())
# dsu = DisjointSetUnion(n)

# for i in range(1, n + 1):
#     dsu.make_set(i)

visited = set()
ribes = {}

for _ in range(m):
    v, u, w = map(int, input().split())
    # dsu.union_sets(v, u, w)
    if v > u:
        v, u = u, v
    key = f'{v}-{u}'

    if v not in visited or u not in visited:
        visited.add(v)
        visited.add(u)
        ribes[key] = w
    

# print(dsu.get_set_mins())
