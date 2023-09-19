'''
https://leetcode.com/problems/summary-ranges/


Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
'''

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        nums.append(nums[-1] + 2)
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                if start != nums[i - 1]:
                    result.append(f"{start}->{nums[i - 1]}")
                else:
                    result.append(f'{start}')
                start = nums[i]
        return result


print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))
