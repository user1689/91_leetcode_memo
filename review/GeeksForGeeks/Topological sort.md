## 题目
https://practice.geeksforgeeks.org/problems/topological-sort/1/#

## 思路
拓扑排序

## python3
```python3
import collections 

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0] * V
        for i in range(0, len(adj)):
            for j in range(0, len(adj[i])):
                indegree[adj[i][j]] += 1
        res = []
        queue = collections.deque()
        for i in range(0, len(indegree)):
            if (indegree[i] == 0):
                queue.append(i)
         
        while (queue):
            v = queue.popleft()
            res.append(v)
            for child in adj[v]:
                indegree[child] -= 1
                if (indegree[child] == 0):
                    queue.append(child)
    
        return res
```

