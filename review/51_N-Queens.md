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
        

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
            
        res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        # select from row
        def backTrack(row, n):
            # base
            if (row == n):
                tmp_res = []
                for tmp in board:
                    tmp_str = ''.join(tmp)
                    tmp_res.append(tmp_str)
                res.append(tmp_res)
            
            for col in range(n):
                if (col in cols or (row + col) in diagonal1 or (row - col) in diagonal2):
                    continue
                cols.add(col)
                diagonal1.add(row + col)
                diagonal2.add(row - col)
                board[row][col] = 'Q'
                backTrack(row + 1, n)
                board[row][col] = '.'
                cols.remove(col)
                diagonal1.remove(row + col)
                diagonal2.remove(row - col)
        
        cols = set()
        diagonal1 = set()
        diagonal2 = set()
        backTrack(0, n)
        return res
```

## 复杂度分析
* time n!
* space n

## 相关题目
1. https://leetcode-cn.com/problems/n-queens-ii/
