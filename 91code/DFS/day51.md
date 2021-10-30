## 题目
https://leetcode-cn.com/problems/as-far-from-land-as-possible/

## 思路
单源朴素BFS, 多源朴素BFS

## python3
```python3
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        # time row * col * (row * col) = n**4
        # space row * col
        def bfs(x, y):
            queue = deque()
            visited = [[False for _ in range(col)] for _ in range(row)]
            queue.append((x, y))
            visited[x][y] = True
            step = 1
            while(queue):
                size = len(queue)
                for _ in range(size):
                    x, y = queue.popleft()
                    for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if 0<=new_x<row and 0<=new_y<col and not visited[new_x][new_y]:
                            visited[new_x][new_y] = True
                            queue.append((new_x, new_y))
                            if grid[new_x][new_y] == 1:
                                return step
                step += 1
            return -1

        row = len(grid)
        col = len(grid[0])
        maxStep = -1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    maxStep = max(maxStep, bfs(i, j))
        return maxStep

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        # time n**2
        # space n**2
        # 朴素多源BFS
        row = len(grid)
        col = len(grid[0])
        queue = collections.deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    queue.append((i, j))
        # corner case
        if len(queue) == 0 or len(queue) == row * col:
            return -1
        
        # 会多算一次 所以设置成-1 可能的解决方案：如果能写在方法里就可以提前return  
        distance = -1
        while (queue):
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                for newX, newY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0<=newX<row and 0<=newY<col:
                        if grid[newX][newY] != 1:
                            grid[newX][newY] = 1
                            queue.append((newX, newY))
            distance += 1
        return distance
```

## 复杂度分析
* time n**2
* space n**2

## 相关题目
1. https://leetcode-cn.com/problems/max-area-of-island/
2. https://leetcode-cn.com/problems/number-of-islands/
