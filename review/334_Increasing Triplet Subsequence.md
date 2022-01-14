## 题目
https://leetcode-cn.com/problems/increasing-triplet-subsequence/

## 思路
travese from two directions

## python3
```python3
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # time n
        # space n
        # traverse from two direction 
        n = len(nums)
        if (n < 3):
            return False
        Arr1 = [0 for _ in range(n)]
        Arr1[0] = nums[0]
        Arr2 = [0 for _ in range(n)]
        Arr2[-1] = nums[-1]
        for i in range(1, len(nums)):
            Arr1[i] = min(Arr1[i - 1], nums[i])
        for j in range(len(nums) - 2, -1, -1):
            Arr2[j] = max(Arr2[j + 1], nums[j])
        for k in range(1, len(nums) - 1):
            if (Arr1[k - 1] < nums[k] < Arr2[k + 1]):
                return True
        return False

```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/longest-increasing-subsequence/
