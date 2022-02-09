## 题目
https://leetcode-cn.com/problems/binary-search-tree-iterator/

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
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while(root):
            self.stack.append(root)
            root = root.left
        
    def next(self) -> int:
        res = self.stack[-1]
        cur = res.right
        self.stack.pop()
        while (cur):
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

## 复杂度分析

## 相关题目
1. https://leetcode-cn.com/problems/flatten-nested-list-iterator/
