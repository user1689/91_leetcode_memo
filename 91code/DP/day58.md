## 题目

## 思路

## python3
```python3
class Solution:
    # 朴素二进制枚举DFS
    # time n*m 
    # space n*m 
    def uniquePaths(self, m: int, n: int) -> int:
        @lru_cache
        def dfs(i, j):
            # base
            if i > m or j > n:
                return 0
            # reach destination
            if i == m - 1 and j == n - 1:
                return 1
            
            down = dfs(1 + i, j)
            right = dfs(i, j + 1)
            return right + down

        return dfs(0, 0)
        
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 状态定义
        # dp[i][j]表示到达坐标的(i,j)的不同路径
        # 状态转移
        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```

## 复杂度分析
* time n**m
* space n*m

## 相关题目
1. https://leetcode-cn.com/problems/unique-paths-ii/
2. https://leetcode-cn.com/problems/minimum-path-sum/
