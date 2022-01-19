## 题目
https://leetcode-cn.com/problems/divide-two-integers/

## 思路
imitation

## python3
```python3
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == 0):
            return 0
        
        # 预判边界
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # 处理符号
        if (dividend < 0) ^ (divisor < 0):
            flag = -1
        else:
            flag = 1

        if (dividend > 0):
            dividend = -dividend
        if (divisor > 0):
            divisor = -divisor
        
        # 倍增
        ans = 0
        while(dividend <= divisor):
            tmp = divisor
            k = 1
            # 记得需要判断tmp+tmp是否合法
            while(dividend <= (tmp * tmp)and tmp >= -2**30):
                tmp += tmp
                k += k
            dividend -= tmp
            ans += k
        
        return ans if flag == 1 else -ans  
```

## 复杂度分析
* time logC * logC
* space 1

## 相关题目
1. 待补充
