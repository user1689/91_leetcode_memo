## 题目
https://leetcode-cn.com/problems/binary-tree-pruning/

## 思路
DFS

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return None

            leftNode = dfs(root.left)
            rightNode = dfs(root.right)
            if not leftNode:
                root.left = None
            if not rightNode:
                root.right = None
 
            return root.val == 1 or leftNode or rightNode
        
        return root if dfs(root) else None
```

## 复杂度分析
* time N
* space H

## 相关题目
1. 待补充
