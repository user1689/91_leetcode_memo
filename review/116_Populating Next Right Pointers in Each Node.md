## 题目
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

## 思路
BFS

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

```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
