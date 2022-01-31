## 题目
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/

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
    def minDepth(self, root: TreeNode) -> int:
        ’‘’
        case1:
        1
         \
          2
           \
            3
             \ 
              5
              
        case2:
            1
           / \
          2   4
         / \ / \ 
        6  7 9 12 
        ‘’‘
        def dfs(root):
            if (not root):
                return 0
            if (not root.left and not root.right):
                return 1
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            # 这里其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回m1 + m2 + 1;
            if (not root.left or not root.right):
                return left_depth + right_depth + 1

            return min(left_depth, right_depth) + 1
        
        return dfs(root)
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
