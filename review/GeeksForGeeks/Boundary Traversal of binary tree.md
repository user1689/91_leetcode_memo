## 题目
https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1/#

## 思路
DFS, preOrder

## python3
```python3
class Solution:
    def printBoundaryView(self, root):
        # Code here
        def leftBoundary(root):
            if (not root):
                return 
            if (not root.left and not root.right):
                return 
            
            if (root.left):
                res.append(root.data)
                leftBoundary(root.left)
            elif (root.right):
                res.append(root.data)
                leftBoundary(root.right)
            
        def rightBoundary(root):
            if (not root):
                return 
            if (not root.left and not root.right):
                return
            
            if (root.right):
                rightBoundary(root.right)
                res.append(root.data)
            elif (root.left):
                rightBoundary(root.left)
                res.append(root.data)
            
        def bottomBoundary(root):
            if (not root):
                return 
            if (not root.left and not root.right):
                res.append(root.data)
            
            bottomBoundary(root.left)
            bottomBoundary(root.right)
 
        
        res = []
        if (root):
            res.append(root.data)
            leftBoundary(root.left)
            # corner case:
            # [1]
            bottomBoundary(root.left)
            bottomBoundary(root.right)
            rightBoundary(root.right)
        return res        
```
