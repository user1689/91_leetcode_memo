## 题目
https://leetcode-cn.com/problems/sort-an-array/

## 思路
quickSort, mergeSort

## python3
```python3
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quickSort
        def partition(low: int, high: int) -> int:
            pivot = random.randint(low, high)
            nums[low], nums[pivot] = nums[pivot], nums[low]
            i = low
            j = low + 1
            while (j <= high):
                if (nums[j] < nums[low]):
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[i], nums[low] = nums[low], nums[i]
            return i

        def quickSort(low: int, high: int):
            if (low < high):
                mid = partition(low, high)
                quickSort(low, mid - 1)
                quickSort(mid + 1, high)

        quickSort(0, len(nums) - 1)
        return nums
```

## 复杂度分析
* time nlogn
* space 1

## 相关题目
1. 待补充
