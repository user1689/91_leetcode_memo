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

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        '''
        10 - 3 
        10 - 3 - 3 = 4 > b   res += 2
        10 - 3 - 3 - 3 - 3 

        4 - 3 = 1 < b   res += 1
        4 - 3 - 3  

        -2147483648 
        -1
        2147483647
        1
        '''
        if (dividend == 0):
            return 0

        if (dividend == -2147483648 and divisor == -1):
            return 2147483647

        neg = False
        if ((dividend < 0) ^ (divisor < 0)):
            neg = True

        if (dividend > 0):
            dividend = -dividend

        if (divisor > 0):
            divisor = -divisor
        
        a = dividend
        b = divisor        
        res = 0
        while (a <= b):
            tmp = b
            k = 1
            while (tmp >= -2**30 and a <= tmp + tmp):
                tmp += tmp
                k += k
            a -= tmp
            res += k
        return res if not neg else -res
```


## 复杂度分析
* time logC * logC
* space 1

## 相关题目
1. 待补充

 
