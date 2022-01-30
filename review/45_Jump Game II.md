## 题目
https://leetcode-cn.com/problems/jump-game-ii/

## 思路
Greedy

## python3
```python3
class Solution:
    # 范围跳跃
    def jump(self, nums: List[int]) -> int:
        # time n
        # space 1
        # Greedy
        n = len(nums)
        end = 0
        farest = 0
        step = 0
        for i in range(0, n - 1):
            farest = max(farest, nums[i] + i)
            if (i == end):
                end = farest
                step += 1
        return step
```

## 复杂度分析
* time n 
* space 1

## 相关题目
1. 待补充
