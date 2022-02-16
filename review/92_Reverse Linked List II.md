## 题目
https://leetcode-cn.com/problems/reverse-linked-list-ii/

## 思路
imitation

## python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        def reverseLinkedlist(node):
            pre = None
            cur = node
            while (cur):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
             
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(0, left - 1):
          pre = pre.next
        
        rightNode = pre
        for _ in range(0, right - left + 1):
            rightNode = rightNode.next
        
        cur = rightNode.next
        leftNode = pre.next
        rightNode.next = None
        pre.next = None
        
        reverseLinkedlist(leftNode)
        
        pre.next = rightNode
        leftNode.next = cur
        
        return dummy.next
        
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
