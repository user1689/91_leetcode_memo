## 题目
https://leetcode-cn.com/problems/n-queens/

## 思路
DFS(BackTracking)

## python3
```python3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def getBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = 'Q'
                board.append(''.join(row))
                row[queens[i]] = '.'
            return board
        
        # try row
        def dfs(r):
            if (r == n):
                board = getBoard()
                solution.append(board)
            else:
                # try col
                for i in range(n):
                    if i in column or r - i in diagonal1 or r + i in diagonal2:
                        continue
                    queens[r] = i
                    column.add(i)
                    diagonal1.add(r - i)
                    diagonal2.add(r + i)
                    dfs(r + 1)
                    column.remove(i)
                    diagonal1.remove(r - i)
                    diagonal2.remove(r + i)

        solution = []
        queens = [-1] * n
        row = ['.'] * n
        diagonal1 = set()
        diagonal2 = set()
        column = set()
        dfs(0)
        return solution
```

## 复杂度分析
* time n!
* space n

## 相关题目
1. https://leetcode-cn.com/problems/n-queens-ii/
