'''
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
'''

from typing import List


# 1й способ решения - метод 2х указателей
class Solution_1:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums) - 1

        if sum(nums) == 0:
            return 0

        i, j = 0, 1
        max_count = index_zero = count_zero = 0

        while j < len(nums):
            while nums[i] == 0 and i < len(nums) - 1:
                i += 1
                j += 1

            while j < len(nums) and (nums[j] == 1 or count_zero == 0):
                if nums[j] == 0:
                    index_zero = j
                    count_zero += 1
                j += 1

            max_count = max(max_count, j - i - count_zero)
            count_zero = 0
            i, j = index_zero, index_zero + 1 if j < len(nums) else j

        return max_count


# 2й способ решения - скользящее окно
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        coefficient = 1
        i = 0

        for j in range(len(nums)):
            coefficient = coefficient if nums[j] else coefficient - 1
            if coefficient < 0:
                coefficient = coefficient if nums[i] else coefficient + 1
                i += 1
        return j - i




print(Solution().longestSubarray([1,1,0,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1,1,1,1]))
print(Solution().longestSubarray([0,0,1,1]))
