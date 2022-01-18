## 题目
https://leetcode-cn.com/problems/longest-increasing-subsequence/

## 思路
dp, Greedy + binarySearch

## python3
```python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time n**2
        # space n
        # DP
        # 状态定义
        # dp[i]表示以i结尾的最长递增子序列
        # 状态转移
        # dp[i] = max(dp[i], dp[j] + 1)
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
                
class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
      # LIS 
      tmp = []
      for num in nums:
          idx = bisect.bisect_left(tmp, num)
          if (idx == len(tmp)):
              tmp.append(num)
          else:
              tmp[idx] = num
      return len(tmp)
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. 待补充
