'''
    https://leetcode.com/problems/merge-intervals/
'''

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        j = 1
        while j < len(intervals):
            x1, y1 = intervals[j - 1]
            x2, y2 = intervals[j]
            if x2 <= y1:
                intervals[j - 1: j + 1] = [[x1, max(y1, y2)]]
                j -= 1
            j += 1
        return intervals


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,3],[2,6],[6,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,4],[0,4]]))
print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
