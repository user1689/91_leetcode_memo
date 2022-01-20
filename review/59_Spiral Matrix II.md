## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
tricky, imitation

## python3
```python3
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for _ in range(n)] for _ in range(n)]
        top = 0
        right = n - 1
        left = 0
        bottom = n - 1
        tmp = 1
        step = n * n
        while(True):
            for i in range(left, right + 1):
                res[top][i] = tmp
                tmp += 1
            top += 1
            if (top > bottom) or (tmp > step):
                break
            for j in range(top, bottom + 1):
                res[j][right] = tmp
                tmp += 1
            right -= 1
            if (right < left) or (tmp > step):
                break
            for k in range(right, left - 1, -1):
                res[bottom][k] = tmp
                tmp += 1
            bottom -= 1
            if (bottom < top) or (tmp > step):
                break
            for l in range(bottom, top - 1, -1):
                res[l][left] = tmp
                tmp += 1
            left += 1
            if (left > right) or (tmp > step):
                break
        return res

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # time n
        # space 1
        # 思路一
        # imitation遍历
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        direction_idx = 0
        row, col = 0, 0
        for i in range(0, n * n):
            matrix[row][col] = i + 1
            new_row = row + direction[direction_idx][0]
            new_col = col + direction[direction_idx][1]
            if new_row < 0 or new_row >= n or new_col < 0 or new_col >= n or matrix[new_row][new_col] != 0:
                direction_idx = (direction_idx + 1) % 4
            row = row + direction[direction_idx][0]
            col = col + direction[direction_idx][1]
        return matrix

```

## 复杂度分析
* time n * m
* space n * m

## 相关题目
1. 待补充
