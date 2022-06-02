## 题目
https://practice.geeksforgeeks.org/problems/find-number-of-times-a-string-occurs-as-a-subsequence3020/1/#

## python3
```python3
#User function Template for python3

class Solution:
    def countWays(self, S1, S2):
        # code here 
        
        def dfs(i, j):
            
            if ((i < 0 and j < 0) or j < 0):
                return 1
            
            if (i < 0):
                return 0
            
            res = 0
            
            if (S1[i] == S2[j]):
                res += dfs(i - 1, j)
                res += dfs(i - 1, j - 1)
            else:
                res += dfs(i - 1, j)
            
            return res
        
        n = len(S1)
        m = len(S2)
        st = [[-1 for _ in range(m)] for _ in range(n)]
        return dfs(n - 1, m - 1)
```
