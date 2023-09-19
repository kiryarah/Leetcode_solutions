'''
    https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
'''

from random import choice
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.nums_dict = defaultdict(list)

    def insert(self, val: int) -> bool:
        is_in = val not in self.nums_dict

        self.nums_dict[val].append(len(self.nums))
        self.nums.append(val)

        return is_in

    def remove(self, val: int) -> bool:
        if val  not in self.nums_dict:
            return False

        index = self.nums_dict[val][-1]
        self.nums_dict[val].pop()

        if not self.nums_dict[val]:
            del self.nums_dict[val]

        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums.pop()

        index = min(index, len(self.nums) - 1)

        if self.nums_dict and self.nums:
            self.nums_dict[self.nums[index]].remove(len(self.nums))
            self.nums_dict[self.nums[index]].append(index)

        return True

    def getRandom(self) -> int:
        return choice(self.nums)


rndset = RandomizedCollection()
print(rndset.insert(1))
print(rndset.insert(1))
print(rndset.remove(1))



# print(rndset.insert(10))
# print(rndset.insert(10))
# print(rndset.insert(20))
# print(rndset.insert(20))
# print(rndset.insert(30))
# print(rndset.insert(30))
# print(rndset.remove(10))
# print(rndset.remove(10))
# print(rndset.remove(30))
# print(rndset.remove(30))


# print(rndset.insert(4))
# print(rndset.insert(3))
# print(rndset.insert(4))
# print(rndset.insert(2))
# print(rndset.insert(4))
# print(rndset.remove(4))
# print(rndset.remove(3))
# print(rndset.remove(4))
# print(rndset.remove(4))

# ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","remove"]
# [[],[4],[3],[4],[2],[4],[4],[3],[4],[4]]

# ["RandomizedCollection","insert","insert","insert","insert","insert","insert","remove","remove","remove","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
# [[],[10],[10],[20],[20],[30],[30],[10],[10],[30],[30],[],[],[],[],[],[],[],[],[],[]]
