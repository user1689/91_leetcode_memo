## 题目
https://leetcode-cn.com/problems/swap-nodes-in-pairs/

## 思路
模拟穿针引线

## python
```python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#写法一 递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # time n
        # space 1
        # 穿针引线 
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead

#写法二 迭代
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # time n
        # space 1
        # 穿针引线
        dummy = ListNode(0, head)
        cur = dummy

        if not head: return 

        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next

            cur.next = node2
            node1.next = node2.next
            node2.next = node1

            cur = cur.next.next
        
        return dummy.next

```

## 复杂度分析
* time n n为链表长度
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
