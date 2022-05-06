## 题目
https://leetcode-cn.com/problems/sliding-window-maximum/

## 思路
monotonicQueue

## python3
```python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]
        q = [0] * 100000
        hh = 0
        tt = -1
        i = 0
        n = len(nums)
        res = []
        while (i < n):
            if (hh <= tt and q[hh] < i - k + 1):
                hh += 1
            while (hh <= tt and nums[q[tt]] < nums[i]):
                tt -= 1
            tt += 1
            q[tt] = i
            if (i >= k - 1):
                res.append(nums[q[hh]])
            i += 1
        return res
```

## 复杂度分析
* time O(N)
* space O(N)

## 相关题目
1. 
