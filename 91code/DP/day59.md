## 题目
https://leetcode-cn.com/problems/knight-probability-in-chessboard/

## 思路
BFS,DFS,DP

## Python3
```python3
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        # time 8**k
        # space n*n
        # dfs

        # @lru_cache(None)
        def dfs(x, y, counts):
          
            if (x, y, counts) in memo:
                return memo[(x, y, counts)]

            if counts == k:
                return 1

            valid = 0
            total = 0
            for newX, newY in [(x + 2, y + 1), (x + 2, y - 1), (x - 1, y + 2), (x + 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y - 2), (x - 1, y - 2)]:
                total += 1
                if 0 <= newX < n and 0 <= newY < n:
                    valid += dfs(newX, newY, counts + 1) 

            memo[(x, y, counts)] = valid / total 
            return memo[(x, y, counts)]

        memo = dict()
        return dfs(row, column, 0)
```

## 复杂度分析
* time 8**k
* space <n*n

## 相关题目
1. https://leetcode-cn.com/problems/out-of-boundary-paths/
