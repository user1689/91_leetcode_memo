## 题目
https://leetcode-cn.com/problems/subsets/

## 思路
bitManipulation

## python3
```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # time n * 2**n
        # space n
        res = []
        sum = 1 << len(nums)
        # 2**n
        for i in range(0, sum):
            tmp = []
            # n
            for j in range(0, len(nums)):
                if (( i >> j ) & 1) == 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res
```

## 复杂度分析
* time n*2**n
* space n

## 相关题目
1. 待补充
