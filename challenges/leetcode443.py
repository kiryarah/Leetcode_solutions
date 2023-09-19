'''
    https://leetcode.com/problems/string-compression/
'''

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        chars.append(float('inf'))

        i, j = 0, 1

        while j < len(chars):
            if chars[j] != chars[j - 1]:
                count = j - i
                count_list = list(str(count))
                if count > 1:
                    chars[i + 1: j] = count_list
                    j = i + len(count_list) + 1
                i = j
            j += 1

        del chars[-1]

        return f'{len(chars)} - {chars}'


print(Solution().compress(["a","a","b","b","c","c","c"]))
print(Solution().compress(["a"]))
print(Solution().compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(Solution().compress(["a","a","a","b","b","a","a"]))
