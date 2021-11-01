## 题目
https://binarysearch.com/problems/Top-View-of-a-Tree

## 思路
DFS+sort+hashTable,BFS+sort+hashTable

## python3
```python3
class Solution:
    def solve(self, root):
        def PreOrder(root, row, col):
            if not root:
                return None
            res.append((col, row, root.val))
            PreOrder(root.left, row + 1, col - 1)
            PreOrder(root.right, row + 1, col + 1)
        
        res = []
        PreOrder(root, 0, 0)

        tmp = sorted(res, key=lambda x:(x[0], x[1], x[2]), reverse = False)
        
        hashTable = defaultdict(list)
        # {col:[root.val]}
        for a in tmp:
            hashTable[a[0]].append(a[2])
        
        ans = []
        for value in hashTable.values():
            ans.append(value[0])
        
        return ans
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        # bfs层序遍历, 得到col,row,value三元组
        
        def bfs(root, row, col):
            queue = collections.deque()
            queue.append((col, row, root))
            while(queue):
                size = len(queue)
                for _ in range(size):
                    col, row, node = queue.popleft()
                    arr.append((col, row, node.val))
                    if node.left:
                        queue.append((col - 1, row + 1, node.left))
                    if node.right:
                        queue.append((col + 1, row + 1, node.right))
        arr = []
        bfs(root, 0, 0)
        # col 为第一关键字升序,row为第二关键字升序,value 为第三关键字升序
        tmp = sorted(arr, key=lambda x:(x[0], x[1], x[2]), reverse = False)
        
        hashTable = defaultdict(list)
        # {col:[root.val]}
        for a in tmp:
            hashTable[a[0]].append(a[2])
        
        ans = []
        for value in hashTable.values():
            ans.append(value[0])
        
        return ans
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree/
