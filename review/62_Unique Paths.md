## 题目
https://leetcode-cn.com/problems/unique-paths/

## 思路
dp

## python3
```python3
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


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # recursive
        def dfs(right, down):
            # base
            if (right, down) in dic:
                return dic[right, down]
            if ((right > n - 1) or (down > m - 1)):
                return 0
            if ((right == n - 1) and (down == m - 1)):
                return 1
            
            rightPath = dfs(right + 1, down)
            downPath = dfs(right, down + 1)
            total = rightPath + downPath
            dic[right, down] = total
            return total

        dic = dict()
        return dfs(0, 0)
```


## 复杂度分析
* time n*m
* space n*m

## 相关题目
1. https://leetcode-cn.com/problems/unique-paths-ii/
2. https://leetcode-cn.com/problems/minimum-path-sum/
