## 题目
https://leetcode-cn.com/problems/target-sum/

## 思路
DFS,DP

## python3
```python3
# 二进制枚举
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(idx, total):
            if (idx, total) in dic:
                return dic[(idx, total)]
                
            if (idx == n):
                if total == target:
                    return 1
                else:
                    return 0

            left = dfs(idx+1, total + nums[idx])
            right = dfs(idx+1, total - nums[idx])
            dic[(idx, total)] = left + right
            return left + right

        dic = dict()
        n = len(nums)
        return dfs(0, 0)

# 全量DP
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if target > total: return 0
        n = len(nums)
        # f[i][j] 代表考虑前 i 个数，当前计算结果为 j 的方案数，令 nums 下标从 1 开始。
        # 那么 f[n][target]为最终答案，f[0][0] = 1 为初始条件：代表不考虑任何数，凑出计算结果为 0 的方案数为 1 种
  
        dp = [[0 for _ in range(2*total+1)] for _ in range(n + 1)]
        dp[0][0 + total] = 1
        for i in range(1, n+1):
            x = nums[i - 1]
            for j in range(-total, total+1):
                if((j - x) + total >= 0):
                    dp[i][j + total] += dp[i - 1][j - x + total]
                if((j + x) + total <= 2 * total):
                    dp[i][j + total] += dp[i - 1][j + x + total]
        # print(dp)
        return dp[n][target + total]

'''
nums = [1,1,1,1,1]
target = 3
[   
     -5 -4 -3 -2 -1  0  1  2  3  4  5
0    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
1    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], 
2    [0, 0, 0, 1, 0, 2, 0, 1, 0, 0, 0], 
3    [0, 0, 1, 0, 3, 0, 3, 0, 1, 0, 0], 
4    [0, 1, 0, 4, 0, 6, 0, 4, 0, 1, 0], 
5    [1, 0, 5, 0, 10, 0, 10, 0, 5, 0, 1]
]
'''

# 优化DP二维
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 状态定义
        # dp[i][j] 代表在数组的前i个数中取元素，使得元素之和为j的方案数
        # 状态转移
        # dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]] (j >= num)
        
        # 设neg为负数部分
        # (sum - neg) - neg = target
        # neg = (sum - target) // 2
        
        # 也可以设pos为正数部分
        # pos - (sum - pos) = target
        # pos = (target + sum) // 2
        
        # 这里设neg
        sum = 0
        for num in nums: sum += num
        diff = (sum - target)
        if diff < 0 or diff % 2 != 0:
            return 0
        neg = diff // 2
        n = len(nums)
        dp = [[0 for _ in range(neg + 1)] for _ in range(n + 1)]

        # 根据状态定义进行初始化
        # dp[0][0]为从数组前0个元素中选取元素，使得元素之和为0的方案数
        # 当没有元素可取的时候，元素和只能为0，所以方案数为1 即没得选也是一种方案
        dp[0][0] = 1

        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(0, neg + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - num]

        #  nums[1,1,1,1,1], neg = 1
        #   j 0  1
        #   [[1, 0]  0
        #  , [1, 1]  1
        #  , [1, 2]  2
        #  , [1, 3]  3
        #  , [1, 4]  4
        #  , [1, 5]] 5
        #            i

        return dp[n][neg]

# 优化DP一维
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
    
        sum = 0
        for num in nums: sum += num
        diff = (sum - target)
        if diff < 0 or diff % 2 != 0:
            return 0
        neg = diff // 2
        
        n = len(nums)
        dp = [0 for _ in range(neg + 1)]
        dp[0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(neg, -1, -1):
                # dp[j] = dp[j]
                if j >= num:
                    dp[j] = dp[j] + dp[j - num]
                else:
                    break
                    
        return dp[neg]
```

## 复杂度分析
* time n*target
* space target

## 相关题目
1. 01背包
2. 背包求组合数
2. https://leetcode-cn.com/problems/expression-add-operators/
