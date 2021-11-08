## 题目
https://leetcode-cn.com/problems/can-i-win/

## 思路
DFS,DP(待补充)

## python3
```python3
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        # 如果所有数字加起来都不满足desiredTotal就提前返回
        totalSum = ((1 + maxChoosableInteger) * maxChoosableInteger) // 2
        if (totalSum < desiredTotal): return False

        def dfs(state, sum, maxChoosableInteger, desiredTotal):
            
            if visited[state] == 2:
                return True
            if visited[state] == 1:
                return False

            for i in range(1, maxChoosableInteger + 1):

                # 如果数字备选了就跳过
                if ((state >> i) & 1): continue
                # 如果选了以后获胜了就提前返回
                if (sum + i >= desiredTotal):
                    visited[state] = 2
                    return True
                # 看看是否会有让对手必输的情况出现
                if (dfs(state + (1<<i), sum + i, maxChoosableInteger, desiredTotal) == False):
                    visited[state] = 2
                    return True

            # 都试过了没有让对手必输的情况就只能返回先手自己输了
            visited[state] = 1
            return False

        # memo
        visited = [None] * (1 << maxChoosableInteger + 1)
        return dfs(0, 0, maxChoosableInteger, desiredTotal)
```

## 时间复杂度
* time 2**21
* space 2**21

## 相关题目
1. https://leetcode-cn.com/problems/predict-the-winner/
2. https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii/
3. stoneGame
