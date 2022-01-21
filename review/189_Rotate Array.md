## 题目
https://leetcode-cn.com/problems/rotate-array/

## 思路
tricky

## python3
```python3
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time n 每个元素被翻转2次即2n
        # space 1
        # 思路一
        # 三次翻转
        n = len(nums)
        k = k % n
        def swap(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        swap(0, n-1)
        # 翻转不是切片!!!
        swap(0, k-1)
        swap(k, n-1)       
```

## 复杂度分析
* time 2n
* space 1

## 相关题目
1. 待补充
