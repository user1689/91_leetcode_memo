## 题目
https://leetcode-cn.com/problems/house-robber/

## 思路
类二进制枚举, DP

## python3
```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 二进制枚举
        maxMoney = 0
        @lru_cache(None)
        def dfs(idx, money, prev):
            nonlocal maxMoney
            
            # 因为idx从0开始 当idx为1时候表示对idx0做完了选择
            # 所以当idx为4时候表示对idx3作出了选择 此时需要再判断下idx3的money是否符合条件 然后再退出循环 如果先退出循环则会有漏掉答案的可能性
            if money > maxMoney:
                maxMoney = money
            
            if idx == len(nums):
                return 
            
            if prev != 1:
                dfs(idx + 1, money + nums[idx], 1)
            dfs(idx + 1, money, 0)

        dfs(0, 0, 0)
        return maxMoney

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        # 二进制枚举
        dic = dict()

        def dfs(idx):            
            if idx >= len(nums):
                return 0
            
            if idx in dic:
                return dic[idx]
            # 分两种情况
            # 1.偷第start个房子，然后只能从第start+2个房子开始偷
            headFirst = nums[idx]
            headFirst += dfs(idx + 2)

            # 2.不偷第start个房子，从第start+1个房子偷
            noFirst = 0
            noFirst += dfs(idx + 1)
            # 取两种情况的最大值
            ans = max(headFirst, noFirst)
            dic[idx] = ans 
            return ans

        return dfs(0)
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])
        return dp[-1]
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/house-robber-ii/
2. https://leetcode-cn.com/problems/house-robber-iii/
