## 题目
https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/

## 思路
DFS, BFS

## python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if (not root):
                return 0

            leftDepth = dfs(root.left) + 1
            rightDepth = dfs(root.right) + 1
            maxDepth = max(leftDepth, rightDepth)
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

    def maxDepth(self, root: TreeNode) -> int:
        # time n
        # space height
        # 思路二
        # BFS
        # q = queue.Queue()
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
* space logn 

## 相关题目
1. 待补充
