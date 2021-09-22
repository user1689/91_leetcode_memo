## 题目
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

## 思路
DFS, BFS

## python
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
# 写法一
    def maxDepth(self, root: TreeNode) -> int:

        def dfs(root):
            if not root: 
                return 0
            if not root.left and not root.right:
                return 1
            
            maxDepth = max(dfs(root.left), dfs(root.right)) + 1
            return maxDepth
        
        return dfs(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
# 写法二
    def maxDepth(self, root: TreeNode) -> int:
        # time n
        # space height
        # 思路二
        # BFS
        if not root: return 0

        q = deque()
        q.append(root)
        step = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            step += 1

        return step
        
```

## 复杂度分析
* time n
* space height/logn

## 相关题目
1. https://leetcode-cn.com/problems/balanced-binary-tree/
2. https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
3. https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
