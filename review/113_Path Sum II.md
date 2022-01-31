## 题目
https://leetcode-cn.com/problems/path-sum-ii/

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        def dfs(root, total, path):
            if not root:
                return 
            if (not root.left and not root.right):
                if (total + root.val == targetSum):
                    res.append(path + [root.val])
        
            dfs(root.left, total + root.val, path + [root.val])
            dfs(root.right, total + root.val, path + [root.val])

        res = []
        dfs(root, 0, [])
        return res
```

## 复杂度分析
* time n
* space logn 

## 相关题目
1. 待补充
