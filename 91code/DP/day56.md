## 题目
https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

## 思路
DP 第II类基本型

## python3
```python3
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        # time n**2
        # space n
        longSub = [1] * len(nums)
        times = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if (nums[j] < nums[i]):
                    # 说明要更新了，出现了新的最长子序列
                    if (longSub[j] + 1 > longSub[i]):
                        longSub[i] = longSub[j] + 1
                        # 次数也需要更新
                        times[i] = times[j]
                    # 又出来一个j2 所有用的lis长度和前面的j1一样
                    elif (longSub[j] + 1 == longSub[i]):
                        # 长度一样就累加上它的次数
                        times[i] += times[j]
       
        # 最后扫一遍统计下
        res = 0
        maxLen = 0
        for i in range(0, len(nums)):
            if (longSub[i] > maxLen):
                maxLen = longSub[i]
                res = times[i]
            elif (longSub[i] == maxLen):
                res += times[i]
        return res

# x x x x j1 x x j2 x x i
# 1 1 1 1 2  1 1  2 1 1 3 longSub
# 1 1 1 1 1  1 1  1 1 1 2 times
```

## 复杂度分析
* time n**2
* space n

## 相关题目
1. https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/
2. https://leetcode-cn.com/problems/longest-increasing-subsequence/
