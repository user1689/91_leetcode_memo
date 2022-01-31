## 题目
https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/

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
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def dfs(left, right):
            if (left > right):
                return None
            mid = left + (right - left) // 2
            root = TreeNode(nums[mid])
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(nums) - 1)
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. https://leetcode-cn.com/problems/balance-a-binary-search-tree/
