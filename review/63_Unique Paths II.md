## 题目
https://leetcode-cn.com/problems/unique-paths-ii/

## 思路
DP

## python3
```python3
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:\
        
        if (obstacleGrid[-1][-1] == 1):
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        if (obstacleGrid[0][0] == 1):
            dp[0][0] = 0
        else:
            dp[0][0] = 1

        for i in range(1, rows):
            if (obstacleGrid[i][0] == 0):
                dp[i][0] = dp[i - 1][0]
            else:
                break
        for j in range(1, cols):
            if (obstacleGrid[0][j] == 0):
                dp[0][j] = dp[0][j - 1]
            else:
                break
        '''
        stdout
        >>>[[1, 1, 1], 
            [1, 0, 1], 
            [1, 1, 2]]
        '''
        for i in range(1, rows):
            for j in range(1, cols):
                if (obstacleGrid[i][j] != 1):
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]
```

## 复杂度分析
* time n*m
* space n

## 相关题目
1. 待补充
