
## 题目
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/

## 思路
imitation

## python3
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        在每一层新建一个dummy 把cur下一层down给串起来
        串完cur的左右子节点需要 移动向后移动cur看是否还有需要串的节点
        每个循环更新一个first的位置 当first为空推出勋魂
        '''
        first = root
        while (first):
            dummy = Node(0)
            down = dummy
            cur = first
            while (cur):
                if (cur.left):
                    down.next = cur.left
                    down = down.next
                if (cur.right):
                    down.next = cur.right
                    down = down.next
                cur = cur.next
            first = dummy.next
        return root
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
