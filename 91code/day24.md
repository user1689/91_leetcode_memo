## 题目
https://binarysearch.com/problems/Delete-Sublist-to-Make-Sum-Divisible-By-K

```
You are given a list of positive integers nums and a positive integer k. Return the length of the shortest sublist (can be empty sublist ) you can delete such that the resulting list's sum is divisible by k. You cannot delete the entire list. If it's not possible, return -1.

Constraints

1 ≤ n ≤ 100,000 where n is the length of nums
Example 1
Input
nums = [1, 8, 6, 4, 5]
k = 7
Output
2
Explanation
We can remove the sublist [6, 4] to get [1, 8, 5] which sums to 14 and is divisible by 7.
```

## 思路
同余定理+前缀和

## python
```python3
class Solution:
    def deleteSublist(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(0, len(nums)):
            total += nums[i]
        
        target = total % k
        preSum = 0
        dic = {0:-1}
        ans = len(nums)
        for i in range(0, len(nums)):
            preSum += nums[i]
            mod = (preSum) % k
            dic[mod] = i
            if (mod + k * int(mod < target) - target) in dic:
                ans = min(ans, i - dic[(mod + k * int(mod < target) - target)])
        return -1 if ans == len(nums) else ans
```

## 复杂度分析
* time n 
* space min(n, k)

## 相关题目
1. https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/
2. https://leetcode-cn.com/problems/continuous-subarray-sum/
