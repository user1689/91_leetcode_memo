## 题目
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## 思路
binarySearch

## python3
```python3
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        left = 0
        right = len(nums) - 1            # L R
        while (left < right):            # 0 1
            mid = (left + right) >> 1
            if (nums[mid] == target):
                right = mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        if (left == right) and (nums[left] == target):
            res.append(left)
        else:
            res.append(-1)

        left = 0
        right = len(nums) - 1            # L R
        while (left < right):            # 0 1
            mid = (left + right + 1) >> 1
            if (nums[mid] == target):
                left = mid
            elif (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1
        if (left == right) and (nums[left] == target):
            res.append(left)
        else:
            res.append(-1)
        return res
```

## 复杂度分析
* time logn
* space n

## 相关题目
1. 待补充
