## 题目
https://www.geeksforgeeks.org/preorder-successor-node-binary-tree/

## python3
```python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root, target):
        stack = []
        prev = None
        while (stack or root):
            while (root):
                if (prev and prev.val == target):
                    return root.val
                stack.append(root)
                prev = root
                root = root.left
            node = stack.pop()
            if (node.right):
                root = node.right
        return -1
        
node1 = TreeNode(12)
node2 = TreeNode(18)
node3 = TreeNode(10)
node4 = TreeNode(1)
node5 = TreeNode(2)

# node1.left = node2
# node2.left = node3
# node3.right = node4
# node4.left = node5

obj = Solution()
obj.preorderTraversal(node1, 12)
```

## 复杂度分析
* time O(N)
* space O(N)

## 相关题目
1. inorder...
