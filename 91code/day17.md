## 题目
https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/

## 思路
DFS,BFS

## python
```python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # time n 
    # space n
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"
        
        return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def dfs(dataList):
            val = dataList.pop(0)
            if val == 'None':
                return None
            
            root = TreeNode(int(val))
            root.left = dfs(dataList)
            root.right = dfs(dataList)
            return root
        
        dataList = data.split(',')
        return dfs(dataList)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

## 时间复杂度分析
* time n
* space n
## 相关题目
1. https://leetcode-cn.com/problems/serialize-and-deserialize-bst/
2. https://leetcode-cn.com/problems/serialize-and-deserialize-n-ary-tree/
