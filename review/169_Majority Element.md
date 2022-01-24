## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
Moore

## python3
```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        element = 0
        for num in nums:
            # load
            if vote > 0 and num == element:
                vote += 1
            # restart
            elif vote == 0:
                element = num
                vote += 1
            # elinimate
            else:
                vote -= 1
        return element
```


## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/majority-element-ii/

