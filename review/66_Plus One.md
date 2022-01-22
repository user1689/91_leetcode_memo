## 题目
https://leetcode-cn.com/problems/plus-one/

## 思路
imitation

## python3
```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
            else:
                if (carry == 1):
                    digits[i] += 1
                carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits
```
## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
