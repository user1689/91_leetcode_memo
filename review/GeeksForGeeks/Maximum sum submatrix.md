## 题目
https://www.geeksforgeeks.org/maximum-sum-submatrix/

## python3
```python3
class Solution:
    def largest_submatrix_sum(self, matrix) -> int:
        n = len(matrix)
        if ( n==0 ):
            return 0
        m = len(matrix[0])
            
        a = [[0 for _ in range(m+1)] for _ in range(n+1)]
        s = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                a[i][j] = matrix[i - 1][j - 1]

        # calculate preSum
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                s[i][j] = s[i][j - 1] + s[i - 1][j] - s[i - 1][j - 1] + a[i][j]
        
        res = 0
        for x1 in range(1, n+1):
            for y1 in range(1, m+1):
                for x2 in range(1, n+1):
                    for y2 in range(1, m+1):
                        res = max(res, s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])
       
        return res

matrix = [[1],[2]]
obj = Solution()
obj.largest_submatrix_sum(matrix)
```

# 时间复杂度
* time n^4
* space n^2

# 相关题目
1. 待补充
