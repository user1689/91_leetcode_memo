## 题目 
https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/

## 思路
BFS

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if (not root):
            return []
        queue = deque([root])
        res = []
        level = 0 
        while (queue):
            tmp = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
            if (level & 1):
                tmp = tmp[::-1]
            level += 1
            res.append(tmp)
        return res

```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
