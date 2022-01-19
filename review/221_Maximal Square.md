## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
bruteForce, dp

## python3
```python3
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxSide = 0
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '1':
                    maxSide = max(maxSide, 1)
                    curMaxSide = min(row - r, col - c)
                    for i in range(1, curMaxSide):
                        flag = True
                        # equals 0
                        if (matrix[r + i][c + i] != '1'):
                            break
                        # equals 1
                        for j in range(0, i):
                            if (matrix[r + i][c + j] == '0' or matrix[r + j][c + i] == '0'):
                                flag = False
                                break
                        if (flag):
                            maxSide = max(maxSide, i + 1)
                        else:
                            break
        return maxSide * maxSide 
```

## 复杂度分析
* time row * col * min(row, col)**2
* space row * col

## 相关题目
1. https://leetcode-cn.com/problems/maximal-rectangle/
