## 题目
https://leetcode-cn.com/problems/powx-n/

## 思路
quickM

## python3
```python3
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        if n < 0: 
            x = 1 / x 
            n = -n
        while(n):
            if (n & 1):
                res *= x
            x *= x
            n >>= 1
        return res
```

## 复杂度分析
* time logn
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/super-pow/
