## 题目
https://leetcode-cn.com/problems/swim-in-rising-water/

## 思路
binaryLeftBoundary+possible+DFS/BFS(check), BFS+PQ

## python3
```python3
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # time 
        # space 
        # 二分+possible
        # 1确定上下界[max(grid[0][0], grid[n-1][n-1]), (n * n) - 1]
        # 2判断是否合理
        # 3二分左界
        def dfs(t, x, y, visited):
            if (x == n - 1 and y == n - 1):
                return True

            visited[x][y] = True

            for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (0 <= new_x < row) and (0 <= new_y <col) and (not visited[new_x][new_y]) and (grid[new_x][new_y] <= t):
                    if dfs(t, new_x, new_y, visited):
                        return True
            return False
            
        row = len(grid)
        col = len(grid[0])
        n = len(grid)
        left, right = max(grid[0][0], grid[n-1][n-1]), (n * n) - 1
        while (left < right):
            mid = (left + right) >> 1
            visited = [[False for _ in range(col)] for _ in range(row)]
            if dfs(mid, 0, 0, visited):
                right = mid
            else:
                left = mid + 1
        return left
```

## 复杂度分析
* time n*m*logn n is row, m is col
* space n*m n is row, m is col

## 相关题目
1. https://leetcode-cn.com/problems/path-with-minimum-effort/
