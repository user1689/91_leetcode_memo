## 题目
https://leetcode-cn.com/problems/find-peak-element/

## 思路
binarySearch

## python3
```python3
class Solution:
    '''
    若采用向后对比
    当nums[i]<nums[i+1]则i位置不可能是峰值 -> left = mid + 1
    当nums[i]>nums[i+1]则i位置有可能是峰值但不一定需要继续往前看看 -> right = mid
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while(left < right):
            
            #向前对比
            # mid = left + (right - left + 1) // 2
            # if nums[mid - 1] < nums[mid]:
            #     left = mid
            # elif nums[mid - 1] > nums[mid]:
            #     right = mid - 1

            #向后对比
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid

        return left 
```

## 复杂度分析
* time logn
* space 1

## 相关题目
1. 待补充
