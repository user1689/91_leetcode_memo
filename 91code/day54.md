## 题目
https://leetcode-cn.com/problems/min-cost-climbing-stairs/

## 思路
DP

## python3
```python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp[i]代表到达位置i的最小体力花费
        # dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        
        n = len(cost)
        # 由于可以选择下标 0 或 1 作为初始阶梯，因此有 dp[0] = dp[1] = 0 
        dp = [0 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # dp[i]代表到达位置i的最小体力花费
        # dp[i] = min(dp[i - 1] + cost[i], dp[i - 2] + cost[i])
        
        n = len(cost)
        prev = cur = 0
        for i in range(2, n + 1):
            nxt = min(cur + cost[i - 1], prev + cost[i - 2])
            prev, cur = cur, nxt
        return nxt

```

## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/climbing-stairs/
