## 题目
https://leetcode-cn.com/problems/jump-game/

## 思路
Greedy, DP

## python3
```python3
class Solution:
    def jumpGame(self, nums : List[int]) --> bool:
        farest = 0
        n = len(nums)
        for i in range(n):
          if farest >= i:
              farest = max(farest, i + nums[i])
        return farest >= n - 1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 状态定义 
        # dp[i] 表示从 0 出发，经过 j <= i，可以跳出的最远距离
        # 状态转移 
        # if dp[i - 1] > i: dp[i] = max(dp[i - 1], i + nums[i])
        # else dp[i] = dp [i - 1]
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            if dp[i - 1] >= i:
                dp[i] = max(dp[i - 1], i + nums[i])
            else:
                dp[i] = dp[i - 1]
        return dp[-1] >= (n - 1)
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/jump-game-ii/
