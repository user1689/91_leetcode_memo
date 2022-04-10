## 题目
https://leetcode-cn.com/problems/container-with-most-water/

## python3
```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        10^9 -> sqrt(n)

        [1,2,3,4,5,6]
        [6,5,4,3,2,1]
        [0,0,0,0,0,0]
        [1,1,1,1,1,1]
        [1,1]
        [0,0]
        +- 奇偶 顺序/排列 空/1 重复 min/max 前导0
        '''
        n = len(height)
        left = 0
        right = n - 1
        max_area = -1
        while (left < right):
            width = right - left
            max_area = max(max_area, min(height[left], height[right]) * width) 
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return max_area
```
## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
