## 题目
https://leetcode-cn.com/problems/search-a-2d-matrix/

## 思路
binarySearch

## python3
```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bianry_search_row(left, right):
            while (left < right):
                mid = (left + right + 1) >> 1
                if (target >= matrix[mid][0]):
                    left = mid 
                else:
                    right = mid - 1
            return left
        
        def bianry_search_col(left, right, row_idx):
            while (left < right):
                mid = (left + right + 1) >> 1
                if (target >= matrix[row_idx][mid]):
                    left = mid 
                else:
                    right = mid - 1
            return left
        
        row = len(matrix) 
        col = len(matrix[0])
        row_idx = bianry_search_row(0, row-1)
        col_idx = bianry_search_col(0, col-1, row_idx)
        return matrix[row_idx][col_idx] == target
```

## 复杂度分析

## 相关题目
1. https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
