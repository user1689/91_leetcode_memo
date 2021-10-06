## 题目
https://leetcode-cn.com/problems/search-insert-position/

## 思路
二分答案，二分区间

## python
```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 二分答案
        # time logn
        # space 1
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:    

        # time logn
        # space 1
        # 二分区间
        if len(nums) == 0:
            return 0
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
        
        if nums[left] >= target:
            return left
        if nums[right] >= target:
            return right
        return right + 1
```
## 复杂度分析
* time logn
* space 1

## 相关题目
1.https://leetcode-cn.com/problems/first-bad-version/
2.https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
3.https://leetcode-cn.com/problems/search-insert-position/
4.https://leetcode-cn.com/problems/guess-number-higher-or-lower/
5.待补充
