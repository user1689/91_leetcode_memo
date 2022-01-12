## 题目
https://leetcode-cn.com/problems/valid-sudoku/

## 思路
hashTable


## python3
```python3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # time  
        # space 
        # imitation

        row = [[0 for _ in range(9)] for _ in range(9)]
        col = [[0 for _ in range(9)] for _ in range(9)]
        smallBox = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]
        # print(smallBox)
        '''
        [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ], 
            
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ], 
            
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        ]
        '''
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if (char != '.'):
                    char = int(char) - 1
                    row[i][char] += 1
                    col[j][char] += 1
                    smallBox[i // 3][j // 3][char] += 1 
                    if (row[i][char] > 1 or col[j][char] > 1 or smallBox[i // 3][j // 3][char] > 1):
                        return False
        return True
```

## 复杂度分析
* time
* space

## 相关题目
1. https://leetcode-cn.com/problems/sudoku-solver/
