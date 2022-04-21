## 题目
https://leetcode-cn.com/problems/number-of-1-bits/

## 思路
DFS

## python3
```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while (n):
            n &= (n - 1)
            ans += 1
        return ans
```

## 复杂度分析
* time 32
* space 1

## 相关题目
1. 待补充
