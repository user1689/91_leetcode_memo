## 题目
https://leetcode-cn.com/problems/longest-common-subsequence

## 思路
DP

## python3
```python3
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (text1[i - 1] == text2[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
```

## 复杂度分析
* time n**2
* space n**2

## 相关题目
1. 待补充
