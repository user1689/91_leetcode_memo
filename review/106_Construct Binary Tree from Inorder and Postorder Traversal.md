## 题目
https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def dfs(inorder_left, inorder_right, postorder_left, postorder_right):
            if (postorder_left > postorder_right):
                return None
            
            postorder_root_idx = postorder_right
            inorder_root_idx = dic[postorder[postorder_root_idx]]

            root = TreeNode(postorder[postorder_root_idx])
            inorder_left_length = inorder_root_idx - inorder_left
            root.left = dfs(inorder_left, inorder_root_idx - 1, postorder_left, postorder_left + inorder_left_length - 1)
            root.right = dfs(inorder_root_idx + 1, inorder_right, postorder_left + inorder_left_length, postorder_root_idx - 1)
            return root
        
        dic = {}
        for idx, num in enumerate(inorder):
            dic[num] = idx
        return dfs(0, len(inorder) - 1, 0, len(postorder) - 1)
```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
