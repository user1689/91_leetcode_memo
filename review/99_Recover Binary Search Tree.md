## 题目
https://leetcode-cn.com/problems/recover-binary-search-tree/

## 思路
inorder_recursive + global variables, inorder_iterative 

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        '''
        两种不同的情况 
        # eg1: 相邻两个交换了
        #  [1,3,2,4]
        # eg2: 非相邻两个交换了
        #  [1,4,3,2]
        '''
        def dfs(root):
            nonlocal first
            nonlocal second
            nonlocal prev
            # base 
            if (root == None):
                return 
            # inorder
            dfs(root.left)

            # start operation
            if (root.val >= prev.val):
                prev = root
            else:
                # first come here
                if (first == None):
                    first = prev
                    second = root
                    prev = root
                else:
                    # if there is other second exception, it
                    # can catch it.
                    second = root
            dfs(root.right)

        first = None
        second = None
        prev = TreeNode(-inf)
        dfs(root)
        first.val, second.val = second.val, first.val
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        firstNode = None
        secondNode = None
        prev = ListNode(-inf)
        # inorder
        stack = []
        while (root or stack):
            while (root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            if (firstNode is None and root.val < prev.val):
                firstNode = prev
                secondNode = root
            if (firstNode and root.val < prev.val):
                secondNode = root
            prev = root
            root = root.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
