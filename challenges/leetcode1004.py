'''
https://leetcode.com/problems/max-consecutive-ones-iii/description/
'''

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0

        for j in range(len(nums)):
            k = k if nums[j] else k - 1
            if k < 0:
                k = k if nums[i] else k + 1
                i += 1
        return j - i + 1


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
