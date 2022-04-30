## 题目
https://practice.geeksforgeeks.org/problems/count-the-paths4332/1/#

## python3
```python3
class Solution:
    def possible_paths(self, edges, n, s, d):
        
        N = 1000
        h = [-1] * N
        e = [0] * N
        ne = [0] * N
        idx = 0
        
        
        def add(a, b):
            nonlocal idx
            e[idx] = b
            ne[idx] = h[a]
            h[a] = idx
            idx += 1
        
        
        for v1, v2 in edges:
            add(v1, v2)
        
        ans = 0
        st = [0] * N
        
        def dfs(u):
            nonlocal ans
            if (u == d):
                ans += 1
                return
            
            st[u] = 1
            i = h[u]
            while (i != -1):
                j = e[i]
                if (not st[j]):
                    dfs(j)
                i = ne[i]
            st[u] = 0
        
        dfs(s)
        return ans
```
