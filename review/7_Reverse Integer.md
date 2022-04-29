## 题目
https://leetcode-cn.com/problems/reverse-integer/

## 思路
imitation

## python3
```python3
class Solution:
    def reverse(self, x: int) -> int:
        '''
        -2147483648
        -214748364 digit > 8

        2147483647
        214748364 digit > 7

        +- max/min 奇偶 顺序 空/1
        '''
        # 余数 = a % b = a - 商 * b = a - 0取整(a / b) * b
        # print(-123 - int(-123 / 10) * 10)

        ans = 0
        while (x != 0):
            digit = x - int(x/10) * 10
            if (ans < 0 and ((ans < -214748364 and digit > 8) or (ans <= -214748365))):
                return 0
            if (ans > 0 and ((ans > 214748364 and digit > 7) or (ans >= 214748365))):
                return 0
            ans = ans * 10 + digit
            x = int(x / 10)
        return ans
```

## 复杂度分析
*time O(logN)
*space O(1)

## 相关题目
1. 待补充
