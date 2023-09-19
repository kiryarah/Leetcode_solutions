'''
https://leetcode.com/problems/maximize-distance-to-closest-person/description/
'''

from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i, j = 0, 1
        max_dist = 0

        while j < len(seats):

            while j < len(seats) - 1 and seats[j] == 0:
                j += 1

            if seats[i] == 0 or seats[j] == 0:
                max_dist = max(max_dist, j - i)
            else:
                max_dist = max(max_dist, (j - i) // 2)
            i, j = j, j + 1

        return max_dist


print(Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
print(Solution().maxDistToClosest([1, 0, 0, 0]))
print(Solution().maxDistToClosest([0, 1]))
print(Solution().maxDistToClosest([1, 1, 0, 1]))
