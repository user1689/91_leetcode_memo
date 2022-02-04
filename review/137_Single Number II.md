## 题目
https://leetcode-cn.com/problems/single-number-ii/

## 思路
bitManipulation

## python3
```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        出现了三次的元素在32位表示上会有三个1
        mod3以后 剩下的如果还有就是答案
        '''
        ans = 0
        for i in range(0, 32):
            total = sum((num & (1 << i)) for num in nums)
            if (total % 3):
                if (i == 31):
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans 
```

## 复杂度分析

## 相关题目
1. https://leetcode-cn.com/problems/single-number/
2. https://leetcode-cn.com/problems/single-number-iii/
