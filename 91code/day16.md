## 题目

## 思路

## python
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # time n
        # space n
        # 思路一
        # 层序遍历 记录并不断更新每行第一个弹出的值
        # corner case
        # [1]
        # [1,null,1]
        # [0,null,-1]
        
        queue = collections.deque([root])
        maxLeftVal = root.val
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                # 只记录每行第一个弹出的root的值
                if i == 0:
                    maxLeftVal = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return maxLeftVal
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        # time n
        # space n
        # 思路二
        # 前序遍历直接搜 

        maxDepth = -1
        ans = 0

        def dfs(root, depth):
            nonlocal ans
            nonlocal maxDepth

            if not root:
                return
                
            if depth > maxDepth:
                maxDepth = depth
                ans = root.val

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 0)
        return ans
```

## 复杂度分析
* time n 
* space n
## 相关题目
1.待补充
