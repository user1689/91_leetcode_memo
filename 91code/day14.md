## 题目
https://leetcode-cn.com/problems/same-tree/

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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 写法一
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if root1 and not root2:
                return False
            if not root1 and root2:
                return False
            if root1.val != root2.val:
                return False

            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)

        return dfs(p, q)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 写法二
        if not p and not q: 
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            queue1 = deque()
            queue2 = deque()
            queue1.append(p)
            queue2.append(q)
            while queue1 and queue2:
                node1 = queue1.popleft()
                node2 = queue2.popleft()
                if node1.val != node2.val:
                    return False

                left_node1, right_node1 = node1.left, node1.right
                left_node2, right_node2 = node2.left, node2.right

                 # 如果用或，两个都为空时，条件还是成立，回返回false
                 # 但是两个为空是相同结构，用异或是判断两边是否不相等，不相等就表示有一个不为空，会返回false.
                if (not left_node1) ^ (not left_node2):
                    return False
                
                if (not right_node1) ^ (not right_node2):
                    return False

                if node1.left:
                    queue1.append(node1.left)
                if node1.right:
                    queue1.append(node1.right)
                if node2.left:
                    queue2.append(node2.left)
                if node2.right:
                    queue2.append(node2.right)
        return True

```

## 复杂度分析
* time n（DFS）
* space h 树的高度（DFS）

## 相关题目
1. 待补充
