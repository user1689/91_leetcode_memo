## 题目
https://leetcode-cn.com/problems/balanced-binary-tree/

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
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        time O(N)
        space O(N)
        '''

        def dfs(root):
            if (not root):
                return 0

            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)

            if (abs(leftDepth - rightDepth) > 1):
                return float('inf')

            return max(leftDepth, rightDepth) + 1

        if (not root):
            return True
        
        return True if dfs(root) != float('inf') else False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        第一种普通解法是nlogn
        第二种optimal是logn就可以完成
        差别在第二种解法在递归到最底部求解高度的同时计算左右子树的高度差
        '''
        def dfs(root):
            nonlocal balance
            if (not root):
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            if (abs(left_depth - right_depth) > 1):
                balance = False
                return -1
            max_depth = max(left_depth, right_depth) + 1
            return max_depth
        if (not root):
            return True
        balance = True
        dfs(root)
        return balance


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        '''
        纯递归求解
        通过catch异常提前返回-1
        只要有个-1最后就返回False
        '''
        if not root: 
            return True
        def dfs(root):
            if not root:
                return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            maxDepth = max(left_depth, right_depth) + 1
            if (left_depth == -1) or (right_depth == -1) or (abs(left_depth - right_depth) > 1):
                maxDepth = -1
            return maxDepth
        return dfs(root) >= 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # time n ** 2
        # space n
        # 思路一
        # 从顶到底
        def dfs(root):
            if not root:
                return 0
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            return max(left_depth, right_depth) + 1
        
        if not root: return True
        return abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
     
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
