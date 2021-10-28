## 题目
https://leetcode-cn.com/problems/n-queens-ii/

## 思路
DFS(backTracking) 

## python3
```python3
class Solution:
    def totalNQueens(self, n: int) -> int:

        def dfs(row):
            if row == n:
                return 1
            else:
                count = 0
                # 枚举每一列
                # similar to permutation
                for j in range(n):
                    # pruning
                    if j not in columns and row + j not in diagonal1 and row - j not in diagonal2:
                        columns.add(j)
                        diagonal1.add(row + j)
                        diagonal2.add(row - j)
                        count += dfs(row + 1)
                        columns.remove(j)
                        diagonal1.remove(row + j)
                        diagonal2.remove(row - j)
                return count

        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        # 枚举每一行
        return dfs(0)
```
## 复杂度分析
* time n!
* space n

## 相关题目
1. https://leetcode-cn.com/problems/n-queens/
