## 题目
https://leetcode-cn.com/problems/coin-change-2/

## 思路
DFS,DP

## python3
```python3
# DFS+MEMO
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # 此题不能直接用memo数组 因为是不考虑顺序的组合问题
        # 即此题中顺序不同的结果都当成一样的，只计算一次
        # 所以此处用字典，将顺序也纳入参考
        memo = dict()
        
        def dfs(startIdx, remains):
            if remains < 0:
                return 0
            
            if (startIdx, remains) in memo:
                return memo[startIdx, remains]
            
            if remains == 0:
                return 1

            res = 0
            for i in range(startIdx, n):
                res += dfs(i, remains - coins[i])

            memo[startIdx, remains] = res
            return memo[startIdx, remains]

        return dfs(0, amount)
        
# 朴素DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 时间复杂度 O(coins * amount * amount)
        # 状态定义
        # dp[i][j] 表示从前i个物品中挑选，凑成j的方案数量
        # 状态转移
        # dp[i][j] = dp[i - 1][j] + dp[i - 1][j - k * coins[i - 1]] 
        # k的取值范围是 ( 1 <= k < (j // coins[i - 1]) )

        n = len(coins)
        # 还是做一个哨兵即不考虑任何物品的情况
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        
        # 初始化
        # 代表从前0个物品中选，组成0的方案数量为1即不选
        dp[0][0] = 1

        # 这里也可以初始化 dp[i][0]都为 1 类似如上
        # 若初始化 dp[i][0]的话j的遍历设置从1开始就可以了
        # 也可以直接合并到递推里面去，只是写法不同，参考的数值都是上一行
        
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(0, amount + 1):
                dp[i][j] = dp[i - 1][j]
                # # 未经过优化
                # k = 1
                # while k * coin <= j:
                #     dp[i][j] += dp[i - 1][j - k * coin]
                #     k += 1

                # 从数学角度推导优化状态转移方程
                # 详见 518题weiwei, 三叶姐姐背包动态规划第四节
                # 为一维优化埋下伏笔
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]
        return dp[n][amount]
        
# 1d DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)
        dp = [0 for _ in range(amount + 1)] 
        dp[0] = 1
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(0, amount + 1):
                if (j >= coin):
                    dp[j] += dp[j - coin]
        return dp[amount]
```

## 复杂度分析
* time n * amount
* space n * amount

## 相关题目
1. 待补充
