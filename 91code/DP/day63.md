## 题目
https://leetcode-cn.com/problems/coin-change/

## 思路
DFS,BFS,DP

## python3
```python3
# DFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def dfs(remains):
            if remains < 0:
                return -1
            if remains == 0:
                return 0
            if memo[remains] != -2:
                return memo[remains]

            res = inf
            for coin in coins:
                curRemains = remains - coin
                if curRemains < 0:
                    break
                nxtRemains = dfs(curRemains)
                if nxtRemains >= 0 and nxtRemains < res:
                    res = nxtRemains + 1
            
            if res != inf:
                memo[remains] = res
            else:
                memo[remains] = -1
            # return res if res != inf else -1
            return memo[remains]
        
        memo = [-2 for _ in range(amount + 1)]
        coins.sort()
        return dfs(amount)
        

# BFS
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def bfs(remains):
            queue = collections.deque()
            queue.append(amount)
            count = 1
            while (queue):
                size = len(queue)
                for _ in range(size):
                    remains = queue.popleft()
                    for coin in coins:
                        curAmount = remains - coin
                        if (curAmount == 0):
                            return count  
                        if (curAmount < 0):
                            break
                        if curAmount not in memo:
                            queue.append(curAmount)
                            memo.add(curAmount)
                count += 1
            else:
                return -1

        if amount < 1: return 0
        memo = set()
        memo.add(amount)
        coins.sort()
        return bfs(amount)


#DP2d
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i][j]表示从前i个硬币中选能凑成j所需的最少个数
        # dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - k * coin] + k)
        
        # 先定义dp数组
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        # 初始化dp数组
        dp[0][0] = 0
        # 如果我们在 INF 的基础上进行累加的话，常规的语言会将其变成负数最小值。
        # 也就是在正无穷基础上进行累加，会丢失其正无穷的含义，这与数学上的正无穷概念冲突。
        # 于是我们有另外一个技巧，不直接使用 INT_MAX 作为 INF，而是使用一个比 INT_MAX 小的较大数来代表 INF
        # 比如使用 0x3f3f3f3f 作为最大值，这样我们使用 INF 做状态转移的时候，就不需要先判断再使用了
        INF = 0x3f3f3f3f
        for i in range(1, amount + 1):
            dp[0][i] = INF

        # 递推开始
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(0, amount + 1):
                dp[i][j] = dp[i - 1][j]

                k = 1
                while (j >= k * coin):
                    # if (dp[i - 1][j - k * coin] != inf):
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - k * coin] + k)
                    k += 1
        
        return dp[n][amount] if dp[n][amount] != INF else -1

# DP1d
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # dp[i][j]表示从前i个硬币中选能凑成j所需的最少个数
        # dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - k * coin] + k)
        
        # 先定义dp数组
        n = len(coins)
        dp = [0 for _ in range(amount + 1)]

        # 初始化dp数组
        dp[0] = 0
        INF = 0x3f3f3f3f
        for i in range(1, amount + 1):
            dp[i] = INF

        # 递推开始
        for i in range(1, n + 1):
            coin = coins[i - 1]
            # for j in range(coin, amount + 1):
            #     dp[j] = min(dp[j], dp[j - coin] + 1)
            for j in range(0, amount + 1):
                if (j >= coin):
                    dp[j] = min(dp[j], dp[j - coin] + 1)
        
        return dp[amount] if dp[amount] != INF else -1

# reference 
# 从数学角度推导「完全背包」与「01 背包」之间的遍历顺序关系
# https://leetcode-cn.com/problems/perfect-squares/solution/dong-tai-gui-hua-bei-bao-wen-ti-qiang-hu-hcmi/（leetcode）
# https://mp.weixin.qq.com/s?__biz=MzU4NDE3MTEyMA==&mid=2247486107&idx=1&sn=e5fa523008fc5588737b7ed801caf4c3&chksm=fd9ca184caeb28926959c0987208a3932ed9c965267ed366b5b82a6fc16d42f1ff40c29db5f1&token=990510480&lang=zh_CN#rd （公众号）
# 强化利用「等差」特性推导「完全背包」的核心要素
# https://mp.weixin.qq.com/s/zWh9zyIGMd-6fzz-KIQGDw（公众号）

# 站在更高的角度看待一般性的背包问题一维空间优化
# https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-bei-bao-wen-ti-zhan-zai-3265/（leetcode）

# 再次总结完全背包一维优化推导的两种方式(1数学即利用等差性质 2换元法) 
# https://leetcode-cn.com/problems/coin-change-2/solution/gong-shui-san-xie-xiang-jie-wan-quan-bei-6hxv/（leetcode）
# 补充3YE完全背包一维优化数学推导
# https://leetcode-cn.com/problems/coin-change/solution/er-wei-zhuan-yi-wei-dpzui-jian-ji-yi-don-3pfv/（leetcode）

```

## 复杂度分析
* time n * amount n is the length of coins
* space amount

## 相关题目
1. https://leetcode-cn.com/problems/coin-change-2/
2. https://leetcode-cn.com/problems/minimum-cost-for-tickets/
