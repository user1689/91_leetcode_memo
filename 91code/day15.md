## 题目
https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/

## 思路
回溯(传递数组/维护全局变量)，BFS双队列

## python3
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # time n
        # space n
        # 写法一
        def backtracking(root, path):
            if not root:
                return
            if not root.left and not root.right:
                res.append(path + [str(root.val)])
                return

            backtracking(root.left, path + [str(root.val)])
            backtracking(root.right, path + [str(root.val)])

        res = []
        backtracking(root, [])
        ans = 0
        for num in res:
            ans += int(''.join(num))
        return ans
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # time n
        # space h
        # 写法二
        # 直接dfs

        if not root: return 0 

        def dfs(root, total):
            nonlocal res
            if not root: return
            if not root.left and not root.right:
                total = total * 10 + root.val
                res += total
                return 

            if root.left:
                dfs(root.left, total * 10 + root.val)
            if root.right:
                dfs(root.right, total * 10 + root.val)

        res = 0
        dfs(root, 0)
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # time n
        # space n
        # 思路二
        # 直接bfs
        # double deque
        if not root: return 0

        queueNode = deque()
        queueNode.append(root)
        queueVal = deque()
        queueVal.append(root.val)
        res = 0
        
        while queueNode:
            node = queueNode.popleft()
            nodeVal = queueVal.popleft()
            if not node.left and not node.right:
                res += nodeVal
            if node.left:
                queueNode.append(node.left)
                queueVal.append(nodeVal * 10 + node.left.val)
            if node.right:
                queueNode.append(node.right)
                queueVal.append(nodeVal * 10 + node.right.val)
        
        return res
```
## 复杂度分析
* time n (backtracking-1)
* space n (backtracking-1)

## 相关题目
1. https://leetcode-cn.com/problems/smallest-string-starting-from-leaf/
2. https://leetcode-cn.com/problems/binary-tree-paths/
3. https://leetcode-cn.com/problems/path-sum/
4. https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
