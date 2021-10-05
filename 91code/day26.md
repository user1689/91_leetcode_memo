## 题目
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

## 思路
双指针

## python
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # time n 
        # space 1
        # 普通解法-双指针
        # 当nums[j]!=nums[i]时才进行转移
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                nums[j + 1] = nums[i]
                j += 1
        return j + 1  
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # time n 
        # space 1
        # 通过解法
        # 通过对比当前项和idx-k项判断是否重复
        # 当k=1时 说明与前1位对比是否重复
        if not nums:
            return 0
        def findlength(nums, k):
            idx = 0
            for x in nums:
                if idx < k or nums[idx - k] != x:
                    nums[idx] = x
                    idx += 1
            return idx
        return findlength(nums, 1)
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
