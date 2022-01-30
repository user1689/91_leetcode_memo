## 题目
https://leetcode-cn.com/problems/symmetric-tree/

## 思路
DFS, BFS

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def dfs(root1, root2):
            if (not root1 and root2):
                return False
            if (not root2 and root1):
                return False
            if (not root1 and not root2):
                return True
            if (root1.val != root2.val):
                return False
                    
            isValid = dfs(root1.left, root2.right)
            isValid = isValid and dfs(root1.right, root2.left)
            return isValid

        return dfs(root.left, root.right)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while (queue):
            node1 = queue.popleft()
            node2 = queue.popleft()
            if (not node1 and not node2):
                continue
            if (not node1 or not node2 or node1.val != node2.val):
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        else:
            return True
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
