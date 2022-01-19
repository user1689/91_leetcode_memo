## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
imitation

## python3
```python3
class Solution:
    def isUgly(self, n: int) -> bool:
        if (n <= 0):
            return False
        primeFactors = [2, 3, 5]
        for factor in primeFactors:
            while (n % factor == 0):
                n //= factor
        return n == 1
```


## 复杂度分析
* time logn
* space n

## 相关题目
1. https://leetcode-cn.com/problems/ugly-number-ii/
2. https://leetcode-cn.com/problems/super-ugly-number/
