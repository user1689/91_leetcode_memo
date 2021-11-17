## 题目
https://leetcode-cn.com/problems/sqrtx/

## 思路
二分区间

## python
```python3
class Solution:
    def mySqrt(self, x: int) -> int:

        # time logn
        # space 1
        # 二分区间
        # 
        if x == 0: return 0
        left, right = 1, x
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid 
        return left
```

## 复杂度分析
* time logn
* space 1

## 相关问题
1. 待补充
