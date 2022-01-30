## 题目
https://leetcode-cn.com/problems/validate-binary-search-tree/

## 思路
recursive + inorder, iterative + inorder

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        在递归过程中
        如果要用递归函数返回些什么值作为答案
        首先需要在base写上返回值
        然后需要在每一层中都接受后向上返回
        最后才能在顶层获得底部某个位置的情况
        '''
        def dfs(root):
            nonlocal prev
            if (not root):
                return True

            flag1 = dfs(root.left)

            if (root.val > prev.val):
                prev = root
            else:
                return False

            flag2 = dfs(root.right)

            if (flag1 ^ flag2):
                return False
            else:
                return True 
        

        prev = TreeNode(-inf)
        return dfs(root)
         
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # res = []
        stack = []
        m = float('-inf')
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                # corner case [2,2,2]
                if tmp.val <= m:
                    return False
                m = tmp.val
                # res.append(tmp.val)
                root = tmp.right
        return True 
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
