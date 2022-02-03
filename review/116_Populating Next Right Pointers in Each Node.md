## 题目
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

## 思路
BFS, DFS

## python3
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (not root):
            return root
        queue = deque([root])
        while (queue):
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if (i < size - 1):
                    node.next = queue[0]
                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
        return root

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(root):
            if not root:
                return 
            leftNode = root.left
            rightNode = root.right
            while (leftNode):
                leftNode.next = rightNode
                leftNode = leftNode.right
                rightNode = rightNode.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
