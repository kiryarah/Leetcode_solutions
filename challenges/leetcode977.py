'''
    https://leetcode.com/problems/squares-of-a-sorted-array/
'''
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        i, j = 0 , len(nums) - 1
        result = [0] * len(nums)

        for index in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                result[index] = nums[i] ** 2
                i += 1
            else:
                result[index] = nums[j] ** 2
                j -= 1
        return result


print(Solution().sortedSquares([-4,-1,0,3,10]))
print(Solution().sortedSquares([-7,-3,2,3,11]))
