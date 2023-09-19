'''
    https://leetcode.com/problems/insert-delete-getrandom-o1/
'''


from random import choice

class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.nums_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.nums_dict:
            return False

        self.nums_dict[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums_dict:
            return False

        index = self.nums_dict[val]
        self.nums_dict[self.nums[-1]] = index
        del self.nums_dict[val]

        self.nums[index], self.nums[-1] = self.nums[-1], self.nums[index]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


rndset = RandomizedSet()
print(rndset.insert(1))
print(rndset.insert(2))
print(rndset.insert(2))
print(rndset.insert(3))
print(rndset.remove(2))
print(rndset.remove(2))
print(rndset.getRandom())
