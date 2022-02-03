## 题目

## 思路
BFS, DFS

## python3
```python3
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        bfs反向思路+inplace
        '''
        row = len(board)
        col = len(board[0])
        queue = collections.deque()
        for i in range(row):
            if (board[i][0] == 'O'):
                queue.append((i, 0))
            if (board[i][col-1] == 'O'):
                queue.append((i, col-1))
        for j in range(col):
            if (board[0][j] == 'O'): 
                queue.append((0, j))
            if (board[row-1][j] == 'O'):
                queue.append((row-1, j))

        visited = [[0 for _ in range(col)] for _ in range(row)]
        while (queue):
            x, y = queue.popleft()
            board[x][y] = '#'
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
                if (0<=new_x<row and 0<=new_y<col):
                    if (board[new_x][new_y] == 'O'):
                        
                        queue.append((new_x, new_y))
                        
        for i in range(row):
            for j in range(col):
                if (board[i][j] == '#'):
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
                    
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 逆反思路
        # 遍历边界上所有的O然后设置成#
        # 再一次遍历board然后把所有其他的O设置成X 并还原#成O

        row = len(board)
        col = len(board[0])
        queue = collections.deque()
        
        # 遍历边界上所有的O然后设置成#
        for i in range(0, row):
            if board[i][0] == 'O':
                queue.append((i, 0))
                board[i][0] = '#'
            if board[i][col - 1] == 'O':
                queue.append((i, col - 1))
                board[i][col - 1] = '#'

        for j in range(0, col):
            if board[0][j] == 'O':
                queue.append((0, j))
                board[0][j] = '#'
            if board[row - 1][j] == 'O':
                queue.append((row - 1, j))
                board[row - 1][j] = '#'
        
        while queue:
            x, y = queue.popleft()
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y -1)]:
                if 0<=new_x<row and 0<=new_y<col and board[new_x][new_y] == 'O':
                    queue.append((new_x, new_y))
                    board[new_x][new_y] = '#'
        
        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        return board  
```

## 复杂度分析
* time row * col
* space 1

## 相关题目
1. 待补充
## 相关题目
