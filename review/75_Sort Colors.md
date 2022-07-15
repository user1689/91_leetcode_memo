## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
threePointers, Sort

## Java
```java
class Solution {
    public void sortColors(int[] nums) {
        int zero = -1; // [i:one]
        int n = nums.length;
        int two = n; // [n-1:two] 
        for (int i = 0; i < two;) {
            if (nums[i] == 1) {
                i++;
            } else if (nums[i] == 2) {
                two--;
                swap(nums, i, two);
            } else if (nums[i] == 0) {
                zero++;
                swap(nums, i, zero);
                i++;
            }
        }
        
    }
    
    public void swap(int[] x, int i, int j) {
        int tmp = x[i];
        x[i] = x[j];
        x[j] = tmp;
    }
}
```

## python3
```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ptr1 = 0
        ptr2 = n - 1
        i = 0
        while(i <= ptr2):
            while(i <= ptr2 and nums[i] == 2):
                nums[ptr2], nums[i] = nums[i], nums[ptr2]
                ptr2 -= 1
            if(nums[i] == 0):
                nums[ptr1], nums[i] = nums[i], nums[ptr1]
            i += 1
        return nums

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(low, mid, high):
            tmp = [0] * (high - low + 1)
            i = low 
            j = mid + 1
            k = 0
            while(i <= mid and j <= high):
                if (nums[i] < nums[j]):
                    tmp[k] = nums[i]
                    i += 1
                else:
                    tmp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                tmp[k] = nums[i]
                k += 1
                i += 1

            while j <= high:
                tmp[k] = nums[j]
                k += 1
                j += 1

            for num in tmp:
                nums[low] = num
                low += 1
            
            # for i in range(k):
            #     nums[low + i] = tmp[i]

        def divide(low, high):
            if (low < high):
                mid = low + (high - low) // 2
                divide(low, mid)
                divide(mid + 1, high)
                merge(low, mid, high)
        
        divide(0, len(nums) - 1)
        return nums

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def partition(low, high):
            pivot = random.randint(low, high)
            nums[low], nums[pivot] = nums[pivot], nums[low]
            i, j = low, low + 1
            while(j <= high):
                if (nums[j] < nums[low]):
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[i], nums[low] = nums[low], nums[i]
            return i 
        
        def quickSort(left, right):
            if(left < right):
                mid = partition(left, right)
                quickSort(left, mid - 1)
                quickSort(mid + 1, right)
            
        quickSort(0, len(nums) - 1)
        return nums
```


## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
