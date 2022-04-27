## 题目
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

## 思路
stack

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.left if root.left else root.right
            node = stack.pop()
            res.append(node.val)
            if (stack and stack[-1].left == node):
                root = stack[-1].right
            else:
                root = None
        return res

```

## 复杂度分析
* time O(N)
* space O(N)

## 相关题目
1. 待补充
