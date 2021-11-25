## 题目
https://leetcode-cn.com/problems/minimize-malware-spread/

## 思路
unionFind

## python3
```python3
class union_find:

    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def find(self, x):
        root = x

        while(self.parent[root] != root):
            root = self.parent[root] 

        while(x != root):
            original_parent = self.parent[x]
            self.parent[x] = root
            x = original_parent
        
        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1

class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        # time 
        # space
        uf = union_find()
        n = len(graph)
        for i in range(n):
            uf.add(i)
            for j in range(i):
                if graph[i][j]:
                    uf.merge(i, j)
        
        print(uf.parent)
        print(uf.size)
        initial.sort()        
        max_size, index, fi = 0, -1, []
        # using fi store father
        # using cnt count the frequency of father 
        cnt = collections.defaultdict(int)
        for init in initial:
            fi.append(uf.find(init))
            cnt[fi[-1]] += 1
        for i in range(len(initial)):
            # eg: self.parent = {0:0 1:0}  
            # cnt[0] = 2
            if cnt[fi[i]] > 1:
                continue
            # using uf.size[father] to compare with max_size
            if uf.size[fi[i]] > max_size:
                max_size = uf.size[fi[i]]
                index = initial[i]
        
        return index if index != -1 else initial[0]
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. https://leetcode-cn.com/problems/bricks-falling-when-hit/
2. https://leetcode-cn.com/problems/rank-transform-of-a-matrix/
