## 题目
https://leetcode-cn.com/problems/spiral-matrix/

## 思路
DFS, tricky

## python3
```python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def check(x, y, di):
            xx, yy = x + directions[di][0], y + directions[di][1]
            if xx < 0 or xx >= row or yy < 0 or yy >= col or (isVisited[xx][yy] == 1):
                return False
            return True
        
        def dfs(x, y, step, di):
            isVisited[x][y] = 1
            res.append(matrix[x][y])
            # base
            if (step == row * col):
                return 

            # new_x, new_y = x + directions[di][0], y + directions[di][1]
            if check(x, y, di):
                new_x, new_y = x + directions[di][0], y + directions[di][1]
                dfs(new_x, new_y, step + 1, di)
            else:
                new_direction = (di + 1) % 4
                dfs(x + directions[new_direction][0], y + directions[new_direction][1], step + 1, new_direction)

        row = len(matrix)
        col = len(matrix[0])
        res = []
        isVisited = [[0 for _ in range(col)] for _ in range(row)]
        directions = [(0,1), (1, 0), (0, -1), (-1,0)]
        dfs(0, 0, 1, 0)
        return res


        
```

## 复杂度分析
* time
* space 

## 相关题目
1. 
