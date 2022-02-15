## 题目
https://leetcode-cn.com/problems/find-k-closest-elements/

## 思路
binarySearch, bruteForce(twoPointers)

## python3
```python3
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # time logn + k 
        # space 1
        # 二分
        # 将问题转化为查找区间的左边界
        # (n - 1) - height + 1 = k
        # heigh = n - k
        
        n = len(arr)
        left, right = 0, n - k
        while left < right:
            mid = left + (right - left) // 2
            # 将左右边界的值进行对比，看哪个离x更近
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left : left + k]   
```

## 复杂度分析
* time logn + k
* space 1

## 相关题目
1. 待补充 
