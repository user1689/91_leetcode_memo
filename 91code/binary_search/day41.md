## 题目
https://binarysearch.com/problems/Kth-Pair-Distance

## 思路
sort + slidingWindow + binarysLeftBoundary

## python3
```python3
class Solution:
    def solve(self, nums, k):
        
        # time nlogn + logn
        # space 1
        
        # find the kth smallest diff pairs
        # diff: [0, max(nums) - min(nums)]
        # binary left boundary
        def countPairs(diff):
            i = 0
            ans = 0
            for j in range(1, len(nums)):
                while (nums[j] - nums[i] > diff):
                    i += 1
                # count pairs eg:1 2 we count it as one pair, so we do not need to add 1
                ans += j - i
            return ans
            
        nums.sort()
        k += 1
        left, right = 0, nums[-1] - nums[0]
        while (left < right):
            mid = (left + right) >> 1
            if countPairs(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
```

## 复杂度分析
* time nlon
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/arranging-coins/
2. https://leetcode-cn.com/problems/koko-eating-bananas/
3. https://binarysearch.com/problems/Minimum-Light-Radius
