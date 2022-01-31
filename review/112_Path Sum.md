## 题目
https://leetcode-cn.com/problems/path-sum/

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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ‘’‘
        在递归调用的时候 需要注意一共递归调用了几层 最好画个图清楚点 否则很容易想当然
        ’‘’
        def dfs(root, total):
            if (not root):
                return False
            if (not root.left and not root.right):
                if (total == targetSum):
                    return True
                else:
                    return False

            # 在写树时候判断值最好只判断当前root的
            # 如果要判断子节点需要先判断是否存在 有点像链表的 判断
            valid = False
            if (root.left):
                valid = dfs(root.left, total + root.left.val) 
            if (root.right):
                valid = valid or dfs(root.right, total + root.right.val)

            return valid

        if not root:
            return False
        return dfs(root, root.val)
       
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, total):
            if (not root):
                return False
            if (not root.left and not root.right):
                if (total + root.val == targetSum):
                    return True
                else:
                    return False

            # 在写树时候判断值最好只判断当前root的
            # 如果要判断子节点需要先判断是否存在 有点像链表的 判断
            valid = False
            if (root.left):
                valid = dfs(root.left, total + root.val) 
            if (root.right):
                valid = valid or dfs(root.right, total + root.val)

            return valid

        if not root:
            return False
        return dfs(root, 0)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root, targetSum):
            if not root:
                return False

            if not root.left and not root.right:
                return targetSum == root.val
            
            return dfs(root.left, targetSum - root.val) or dfs(root.right, targetSum - root.val)

        return dfs(root, targetSum)
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
