## 题目
https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list/

## 思路
imitation

## python3
```python3
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(head : Node, insertVal : int) -> Node:
        # case1
        # head is None
        if (not head):
            newNode = Node(insertVal)
            newNode.next = newNode

        # case2
        # node can be inserted into circle
        prev = head
        cur = head.next
        Flag = False

        while True:
            if (prev.val <= insertVal <= cur.val):
                Flag = True
            elif (prev.val > cur.val):
                if (insertVal >= prev.val or insertVal <= cur.val):
                    Flag = True

            if (Flag):
                pre.next = Node(insertVal, cur)
                return head

            prev = cur
            cur = cur.next

            if (head == prev):
                break

        # case3
        # each node has same val in circle, it also can be inserted into circle
        prev.next = Node(insertVal, cur)
        return head
        
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
