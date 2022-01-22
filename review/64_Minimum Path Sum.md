## 题目
https://leetcode-cn.com/problems/minimum-path-sum/

## 思路
DP, DFS

## python3
```python3
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp 表示到达(i, j)需要的最小步数
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        # print(dp)
        # [[1, 4, 5], 
        #  [2, 0, 0], 
        #  [6, 0, 0]]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        def dfs(i, j, visited):
            if (visited[i][j] != 0):
                return visited[i][j]

            if (i == rows or j == cols):
                return float('inf')

            if (i == rows - 1 and j == cols - 1):
                return grid[i][j]
            
            res = grid[i][j]
            down = dfs(i + 1, j, visited)
            right = dfs(i, j + 1, visited)
            res += min(right, down)
            visited[i][j] = res
            return res

        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        return dfs(0, 0, visited)
```

## 复杂度分析
* time n*m
* space n*m

## 相关题目
1. 待补充
