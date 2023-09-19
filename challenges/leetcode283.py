'''
    https://leetcode.com/problems/move-zeroes/
'''

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_none_zero_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_none_zero_index] = nums[i]
                last_none_zero_index += 1

        nums[last_none_zero_index:] = [0] * (len(nums) - last_none_zero_index)


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)

nums = [0]
Solution().moveZeroes(nums)
print(nums)
