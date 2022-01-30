## 题目
https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        1. 建立哈希表加速查找
        2. 根据inorder_idx求出左子树的长度 然后就可以计算出各个部分的idx
        '''
        def dfs(preorder_left, preorder_right, inorder_left, inorder_right):

            if (preorder_left > preorder_right):
                return None
            
            preorder_root_idx = preorder_left
            inorder_root_idx = dic[preorder[preorder_root_idx]]

            root = TreeNode(preorder[preorder_root_idx])
            # 根据inorder求出左子树的长度
            inorder_left_length = inorder_root_idx - inorder_left 
            root.left = dfs(preorder_left + 1, preorder_left + inorder_left_length, inorder_left, inorder_root_idx - 1) 
            root.right = dfs(preorder_left + inorder_left_length + 1, preorder_right, inorder_root_idx + 1, inorder_right)
            return root

        dic = {}
        for idx, num in enumerate(inorder):
            dic[num] = idx
        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
