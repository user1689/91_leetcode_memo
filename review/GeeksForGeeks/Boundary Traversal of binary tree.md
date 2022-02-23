## 题目
https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1/#

## 思路

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
                print(root.data)
                leftBoundary(root.left)
            elif (root.right):
                print(root.data)
                leftBoundary(root.right)
            
        def rightBoundary(root):
            if (not root):
                return 
            if (not root.left and not root.right):
                return
            
            if (root.right):
                rightBoundary(root.right)
                print(root.data)
            elif (root.left):
                rightBoundary(root.left)
                print(root.data)
            
        # def bottomBoundary(root):
        #     if (not root):
        #         return 
        #     if (not root.left and not root.right):
        #         print(root.data)
            
        #     bottomBoundary(root.left)
        #     bottomBoundary(root.right)
        
        def printLeaves(root):
            if(root):
                printLeaves(root.left)
                 
                # Print it if it is a leaf node
                if root.left is None and root.right is None:
                    print(root.data),
         
                printLeaves(root.right)
        
        if (root):
            print(root.data)
            leftBoundary(root.left)
            printLeaves(root.left)
            printLeaves(root.right)
            rightBoundary(root.right)
```
