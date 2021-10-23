## 题目
https://leetcode-cn.com/problems/new-21-game/solution/

## 思路
slidingWindow + DP + probability

## python3
```python3
class Solution:
    def new21Game(self, maxPoints: int, conditionCanChoose: int, chooseRange: int) -> float:
        # DP
        # 状态定义
        # dp[i] 表示当前点数为i 再抽卡不大于N的概率
        # 状态转移
        # eg: W = 10, K = 17, N = 21
        # dp[16] 表示当前点数为16 再抽卡不大于N的概率
        # 后往前推最大的只能为dp[16], 当点数为17就不能抽了 所以后面大于N的概率是固定的
            #        = 1/W  *  ...
            #                  17  18  19  20  21  22  23  24  25  26
            # dp[16] = 1/10 * (1 + 1 + 1 + 1 + 1 + 0 + 0 + 0 + 0 + 0)
            # dp[i]  = 1/W  * (dp[i+1] + ... + dp[i+W]) 
       # dp[15] = 1/10 * (dp[16] + 1 + 1 + 1 + 1 + 1 + 0 + 0 + 0 + 0)
       # dp[i-1] = 1/10 * (dp[i] + dp[i + 1] + ... + + dp[i + W - 1])
       # 求dp[0]

        # 定义数组
        dp = [0.0] * (conditionCanChoose + chooseRange)
        # 因为 conditionCanChoose <= maxPoints
        # 所以可以优化
        # dp = [0.0] * (maxPoints + chooseRange)

        # 初始化
        for i in range(conditionCanChoose, min(maxPoints + 1, conditionCanChoose + chooseRange)):
            dp[i] = 1.0
        
        S = min(maxPoints - conditionCanChoose + 1, chooseRange)
        for i in range(conditionCanChoose - 1, -1, -1):
            dp[i] = S / float(chooseRange)
            S += dp[i] - dp[i + chooseRange]983. Minimum Cost For Tickets
            # tmp = 0
            # for j in range(1, chooseRange+1):
            #     # 从dp[conditionCanChoose - 1]向后算
            #     # 即dp[i + j]
            #     tmp += dp[i + j]
            # dp[i] = tmp/float(chooseRange)

        return dp[0]
```

## 复杂度分析
* time min(maxPoints+1, conditionCanChoose + chooseRange)
* space n

## 相关题目
1. https://leetcode-cn.com/problems/minimum-cost-for-tickets/
