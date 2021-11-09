## 题目
https://leetcode-cn.com/problems/partition-equal-subset-sum/

## 思路
DFS+memo,DP

## python3
```python3

# DFS
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # time 2**n
        # space n 
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        @lru_cache(None)
        def dfs(idx, curSum):
            if curSum > target or idx == n:
                return False
            
            if curSum == target:
                return True

            if dfs(idx+1, curSum+nums[idx]) or dfs(idx+1, curSum):
                return True

            return False
            
        n = len(nums)
        return dfs(0, 0)
        
        
# DP
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        if sum & 1:
            return False
        target = sum // 2
        n = len(nums)

        dp = [False for _ in range(target + 1)]

        # 依据状态定义做判断:
        # 因为下标[0,0]中nums[0]凑不出0所以设置成False
        # 如果依据状态转移则可以理解为:
        # [j - nums[i]] == 0 表示nums[i]恰好为一组,其余为一组,刚才凑成,所以True没问题
        dp[0] = True

        # 先填表格第 0 行，第 1 个数只能让容积为它自己的背包恰好装满
        if nums[0] <= target:
            dp[nums[0]] = True
        
        for i in range(1, n):
            for j in range(target, -1, -1):
                #「从后向前」 写的过程中，一旦 nums[i] <= j 不满足，可以马上退出当前循环
                # 因为后面的 j 的值肯定越来越小，没有必要继续做判断，直接进入外层循环的下一层。
                # 相当于也是一个剪枝，这一点是「从前向后」填表所不具备的。
                if nums[i] <= j:
                    dp[j] = dp[j] or dp[j - nums[i]]
                else:
                    break

        return dp[-1]
```

## 复杂度分析
* time n * target
* space target

## 相关题目
1.https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/
2.01背包

