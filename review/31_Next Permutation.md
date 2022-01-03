## 题目
https://leetcode-cn.com/problems/next-permutation/

## 思路
nextPermutation

## python3
```python3
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(i, j):
            while(i < j):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        # 找到第一个拐点
        firstIdx = -1
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] < nums[i + 1]):
                firstIdx = i
                break
        # 如果没有找到则直接翻转
        if (firstIdx == -1):
            reverse(0, len(nums) - 1)
            return nums
        # 调换第一个大于拐点的数字
        secondIdx = -1
        for j in range(len(nums) - 1, firstIdx, -1):
            if (nums[j] > nums[firstIdx]):
                secondIdx = j
                break
        nums[firstIdx], nums[secondIdx] = nums[secondIdx], nums[firstIdx]
        # 将拐点后剩下的部分直接翻转(排序)
        reverse(firstIdx + 1, len(nums) - 1)
        return nums
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
