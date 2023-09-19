'''
https://leetcode.com/problems/find-k-closest-elements/description/
'''

class Solution(object):
    def findClosestElements(self, arr, k, x):

        if x <= arr[0]:
            return arr[: k]
        if x >= arr[-1]:
            return arr[-k:]

        left, right = 0, len(arr) - 1
        while right - left + 1 > k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            else:
                left += 1
        return arr[left: right + 1]


print(Solution().findClosestElements([1,2,3,4,5], 4, 3))
print(Solution().findClosestElements([1,2,3,4,5], 4, -1))
print(Solution().findClosestElements([1,2,3,4,5], 4, 6))
