## 题目
https://leetcode-cn.com/problems/sort-an-array/

## 思路
quickSort, mergeSort

## python3
```python3
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def partition(low, high):
            pivot = random.randint(low, high)
            swap(pivot, low)
            i, j = low, low + 1
            while j <= high:
                if nums[j] < nums[low]:
                    swap(j, i + 1)
                    i += 1
                j += 1
            swap(low, i)
            return i

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def quickSort(low, high):
            if low < high:
                mid = partition(low, high)
                quickSort(low, mid - 1)
                quickSort(mid + 1, high)
        
        quickSort(0, len(nums) - 1)
        return nums
        
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(low, high):
            if low < high:
                mid = low + (high - low) // 2
                divide(low, mid)
                divide(mid + 1, high)
                merge(low, mid, high)
                
        def merge(low, mid, high):
            tmp = [0] * (high - low + 1)
            i, j = low, mid + 1
            k = 0
            while i <= mid and j <= high:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    k += 1
                    i += 1
                    
                # elif nums[i] > nums[j]:
                else:
                    tmp[k] = nums[j]
                    k += 1
                    j += 1
                    
            while i <= mid:
                tmp[k] = nums[i]
                k += 1
                i += 1

            while j <= high:
                tmp[k] = nums[j]
                k += 1
                j += 1
            
            for i in range(len(tmp)):
                nums[low + i] = tmp[i]

        divide(0, len(nums) - 1)
        return nums
```

## 时间复杂度
* time nlogn
* space logn

## 相关题目
1. 待补充
