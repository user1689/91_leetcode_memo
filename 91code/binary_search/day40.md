## 题目
https://binarysearch.com/problems/Minimum-Light-Radius

## 思路
二分左界 

## python3
```python3
class Solution:
    def solve(self, nums):
        # ┭┮﹏┭┮
        def possible(diameter):
            start = nums[0] 
            end = start + diameter
            n = len(nums)
            # it will iterate 3 times, becasue the number of lights is 3.
            for i in range(3):
                idx = bisect.bisect_right(nums, end)
                # if (idx>=n), it means that this diameter is ok, and then we need to try out whether there is a smaller one diameter.
                if (idx >= n):
                    return True
                start = nums[idx]
                end = start + diameter

        nums.sort()
        if len(nums) <= 3:
            return 0
        # min diameter, max diameter
        left, right = 0, nums[-1] - nums[0] 
        while (left < right):
            mid = left + (right - left) // 2
            if (possible(mid)):
                right = mid
            else:
                left = mid + 1
        # because we use diameter to calculate the answer, so we need to restore it to radius.
        return left / 2
```

## 时间复杂度
* time nlogn
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/koko-eating-bananas/description/
