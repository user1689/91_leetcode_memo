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
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if (not p and not q):
            return True
        elif (not p and q):
            return False
        elif (p and not q):
            return False
        elif (p.val != q.val):
            return False
        else:
            queue1 = deque()
            queue2 = deque()
            queue1.append(p)
            queue2.append(q)
            while (queue1 and queue2):
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                if (node1.val != node2.val):
                    return False
                if (not node1.left) ^ (not node2.left):
                    return False
                if (not node1.right) ^ (not node2.right):
                    return False
                if (node1.left):
                    queue1.append(node1.left)
                if (node1.right):
                    queue1.append(node1.right)
                if (node2.left):
                    queue2.append(node2.left)
                if (node2.right):
                    queue2.append(node2.right)
            else:
                return True
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
