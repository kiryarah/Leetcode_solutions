'''
    https://leetcode.com/problems/number-of-islands/
'''

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == '0' or visited[i][j]:
                return

            visited[i][j] = True

            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)


        n, m = len(grid), len(grid[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    dfs(i, j)

        return count


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))
