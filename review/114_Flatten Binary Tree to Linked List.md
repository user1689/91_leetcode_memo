## 题目
https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        思路一 暴力求解
        思路二 inorder+iteration 利用prev和cur的关系 现在第一轮存下left,right在stack中 然后再第二轮遍历有prev的时候 将prev.left连接到node(栈顶pop出的元素) <-- left, right] 
        思路三 左子树的最下最右的节点，是右子树的父节点
        '''
        stack = [root]
        prev = None
        while (stack):
            node = stack.pop()
            cur = node 
            if (prev):
                prev.left = None
                prev.right = cur
            left = node.left
            right = node.right
            if (right):
                stack.append(right)
            if (left):
                stack.append(left)
            prev = cur    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                pre = nxt = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
