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
        
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        dp表示到i花费最小的步数
        '''
        dp = [0x3f3f3f3f] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if (j + nums[j] >= i):
                    if (dp[i] > dp[j] + 1):
                        dp[i] = dp[j] + 1
        return dp[len(nums) - 1]

class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        [2,3,1,1,4]

        [1]

        farest = 2 -> 4
        维护最远元素 在可以跳到的最远的范围里里 继续找最远元素 
        x x1 x2 
        eg:2, 2, 4, 1, 1, 1, 2

        假设x能到达 x1, x2 并且x2是x1的两倍 x1更新了最远元素 那么x2会在以x1参考的最远元素范围内被考虑 错错错错! 此时需要维护x可以到达范围内所有元素的
        能到达最远距离 选在此范围内起跳能到达最远距离的点farIdx作为下次起点
        '''
        if (len(nums) == 1):
            return 0
        farest = nums[0]
        farIdx = -1
        step = 0
        i = 0
        while (i < len(nums)):
            if (farest >= len(nums) - 1):
                step += 1
                break  
            for j in range(i, i + nums[i] + 1):
                if (j + nums[j] > farest):
                    farest = j + nums[j]  
                    farIdx = j    
            i = farIdx
            step += 1
        return step
```

## 复杂度分析
* time n 
* space 1

## 相关题目
1. 待补充
