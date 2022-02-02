## 题目
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

## 思路
binarySearch

## python3
```python3
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # time logn
        # space 1
        # 思路一
        # 二分查找 当找到就收缩要找的相反边界

        # 选这俩是因为不会出现越界情况，即[1,2]
        #                               R L
        
        if len(nums) == 0: return [-1, -1]

        # left, right = 0, len(nums) - 1
        # # lbound
        # while (left < right):
        #     mid = left + (right - left) // 2
        #     if nums[mid] >= target:
        #         right = mid
        #     else:
        #         left = mid + 1

        # if nums[left] == target: 
        #     lbound = left 
        # else:
        #     lbound = -1
        
        # left, right = 0, len(nums) - 1
        # # rbound
        # while (left < right):
        #     mid = left + (right - left + 1) // 2
        #     if nums[mid] <= target:
        #         left = mid
        #     else:
        #         right = mid - 1
        
        # if nums[left] == target:
        #     rbound = right
        # else:
        #     rbound = -1

        # return [lbound, rbound]



        # 写法二
        # lbound
        lbound, rbound = -1, -1
        left, right = 0, len(nums) - 1
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid

        if nums[left] == target:
            lbound = left
        elif nums[right] == target:
            lbound = right
        else:
            return [-1, -1]

        # rbound
        left, right = 0, len(nums) - 1
        while(left + 1 < right):
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
        
        # 找rbound得先写right, 否则在下面的例子中就就会直接返回left坐标导致lbound和rbound相同。
        # corner case:
        # [2,2]
        #  2
        if nums[right] == target:
            rbound = right
        elif nums[left] == target:
            rbound = left
        else:
            return [-1, -1]
        
        return[lbound, rbound]
        
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
