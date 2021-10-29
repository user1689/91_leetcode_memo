## 题目
https://leetcode-cn.com/problems/max-area-of-island/

## 思路
DFS

## python3
```python3
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        # 参考了@佩奇inging代码发现了原来不通过的问题┭┮﹏┭┮
        def dfs(grid, r, c):
            ans = 1
            # 一进入就需要设置成0 不然会重复计算
            grid[r][c] = 0
            for x, y in[(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if (0<=x<len(grid) and 0<=y<len(grid[0])):
                    if grid[x][y] == 1:
                        ans += dfs(grid, x, y)
            return ans

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(dfs(grid, i, j), ans)
        return ans
        
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(x, y):
            if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] != 1:
                return 0
            grid[x][y] = 0
            res = 1
            for newX, newY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    res += dfs(newX, newY)
            return res

        row = len(grid)
        col = len(grid[0])
        maxSize = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    maxSize = max(dfs(i, j), maxSize)
        return maxSize     
```

## 复杂度分析
* time row * col
* space 1

## 相关问题
1. https://leetcode-cn.com/problems/number-of-islands/
2. https://leetcode-cn.com/problems/island-perimeter/
