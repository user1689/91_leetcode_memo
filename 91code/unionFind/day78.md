## 题目
https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected/

## 思路
unionFind

## python3
```python3
class union_find:

    def __init__(self, size):
        self.father = [None]*size
        self.size = size
    
    def find(self, x):
        if self.father[x] is None:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def merge(self, x, y):
        xx, yy = self.find(x), self.find(y)
        if xx != yy:
            self.father[xx] = yy
            self.size -= 1


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # time n
        # space n
        uf = union_find(n)
        if len(connections) < n - 1: return -1
        for i, j in connections:
            if uf.is_connected(i, j):
                continue
            uf.merge(i, j)
        
        return uf.size - 1
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column/
