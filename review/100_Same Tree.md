## 题目
https://leetcode-cn.com/problems/same-tree/

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def dfs(p, q):
            if (not p and q):
                return False
            if (p and not q):
                return False
            if (not p or not q):
                return True
            if (p.val != q.val):
                return False
            
            isValid = dfs(p.left, q.left) and dfs(p.right, q.right)
            
            if (not isValid):
                return False
            else:
                return True

        return dfs(p, q)
        '''
        case1:    
          1    1       
         /    /
        2    1

        case2:
          1    1
         / \     \
        2   3     3
        '''
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
