## 题目
https://leetcode-cn.com/problems/single-number-iii/

## 思路
bitManipulation

## python3
```python3  
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:

        # 获得ans1 ^ ans2的结果
        target = 0
        for num in nums:
            target ^= num

        # 获取不同的最后一位 用于分组  
        groupDivider = target & (-target)
        num1 = num2 = 0
        for num in nums:
            # 表示只有这个位置没有1 所以&出来的结果为0
            if num & (groupDivider) == 0:
                num1 ^= num
            # 如果这个位置有1 那么&出来的结果就不为0 可以是很多种情况
            else:
                num2 ^= num
                
        return [num1, num2]
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/single-number/
2. https://leetcode-cn.com/problems/single-number-ii/
