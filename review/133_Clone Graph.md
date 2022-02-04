## 题目
https://leetcode-cn.com/problems/clone-graph/

## 思路
DFS, BFS

## python3
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        防止重复遍历 使用map来优化
        {node.val:node}
        当遍历到重复节点我们直接返回node即可
        '''
        def dfs(node):
            if not node:
                return node
            if node.val in dic:
                return dic[node.val] 
            curNode = Node(node.val, None)
            dic[curNode.val] = curNode
            for n in node.neighbors:
                curNode.neighbors.append(dfs(n))
            return curNode

        dic = dict()
        return dfs(node)
        
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # time n
        # space n
        
        '''
        {node:clone}
        直接进行BFS
        '''
        dic = dict()
        queue = deque()
        if not node:
            return
        
        # 新建node 并加入字典
        clone = Node(node.val, [])
        dic[node] = clone
        # 将原始node加入队列
        queue.append(node)
        
        # BFS
        while queue:
            x = queue.popleft()
            # 查看原始node的邻居节点
            for neighbor in x.neighbors:
                # 如果原始node的邻居节点没有被访问过
                # 如果没有被访问过
                # 克隆原始node的邻居节点 并同时加入字典和队列待搜索它的邻居节点
                if neighbor not in dic:
                    neighbor_clone = Node(neighbor.val, [])
                    dic[neighbor] = neighbor_clone
                    queue.append(neighbor)
                # 将他们加入克隆的node的邻居节点列表
                dic[x].neighbors.append(dic[neighbor])
        
        return dic[node]
```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
