## 题目
https://leetcode-cn.com/problems/binary-gap/

## 思路
bitmanipulation

## python3
```python3
class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        j = -1
        for i in range(0, 31):
            if ((n >> i) & 1):
                if (j != -1):
                    ans = max(ans, i - j)
                j = i
        return ans
```

## 复杂度分析
* time O(logN)
* space O(1)

## 相关题目
1. 待补充
