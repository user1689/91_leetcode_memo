## 题目
https://leetcode-cn.com/problems/possible-bipartition/

## 思路
无向图染色

## python3
```python3
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # time V + E
        # space V + E 
        # 染色法+DFS
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        uncolor, red, green = 0, 1, 2 
        c = [uncolor for _ in range(n + 1)]
        valid = True
        
        def dfs(key: int, color: int):
            nonlocal valid
            c[key] = color
            cNei = (green if color == red else red)
            for neighbor in graph[key]:
                if c[neighbor] == uncolor:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                else:
                    if c[neighbor] != cNei:
                        valid = False
                        return 
        
        for key, value in graph.items():
            if c[key] == uncolor:
                    dfs(key, red)
                    if not valid:
                        break
        return valid
        
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # time V + E
        # space V + E
        # 写法二 check函数
        
        graph = [[] for _ in range(n + 1)]
        vis = [0 for _ in range(n + 1)]

        for v, u in dislikes:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node: int, color: int):
            vis[node] = color
            for neighbor in graph[node]:
                if (vis[neighbor] != 0 and vis[neighbor] != -color) or (vis[neighbor] == 0 and not dfs(neighbor, -color)):
                    return False
            return True

        # 一False为False 
        for k in range(1, n + 1):
            if vis[k] == 0 and (not dfs(k, 1)):
                return False
        return True
```
## 复杂度分析
* time V + E
* space V + E

## 相关题目
1. https://leetcode-cn.com/problems/is-graph-bipartite/
