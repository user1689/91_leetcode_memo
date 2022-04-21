## 题目
https://leetcode-cn.com/problems/reverse-bits/

## python3
```python3
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if (n & 1):
                ans = ans << 1
                ans = ans | 1
            else:
                ans = ans << 1
            n = n >> 1
        return ans
        
        # ans = 0
        # while (n):
        #     ans = ans | n & (-n)
        #     n = n & (n - 1)
        # return ans
```

## 复杂度分析
* time O(32)
* space 

## 相关题目
1.待补充
