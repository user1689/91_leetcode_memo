## 题目
https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/

## 思路
DFS

## python
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # dfs遍历, 得到col,row,value三元组
        arr = []
        def dfs(root, row, col):
            if not root:
                return
            arr.append([col, row, root.val])
            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)
        dfs(root, 0, 0)

        # col 为第一关键字升序,row为第二关键字升序,value 为第三关键字升序
        arr = sorted(arr, key=lambda x: (x[0], x[1], x[2]), reverse=False)

        hash_ = defaultdict(list)
        # 同列存到字典,key为col,value为[val]
        for i in arr:
            hash_[i[0]].append(i[2])

        res = []
        # 遍历一下拿出来
        for i in hash_.values():
            res.append(i)

        return res
```

## 复杂度分析
* time nlogn
* space n 

## 相关题目
1. 待补充
