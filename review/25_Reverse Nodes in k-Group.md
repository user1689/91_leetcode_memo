## 题目
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

## 思路
imitation
注意需要先用nxt指向cur.next否则cur.next=cur.next.next时断开就无法找到cur.next了

## python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        
        while head:
            tmp = k
            tail = pre
            while(tmp > 0):
                tail = tail.next
                tmp -= 1
                if not tail:
                    return dummy.next

            nxt = tail.next
            head, tail = self.reverse(head, tail)

            pre.next = head
            tail.next = nxt

            pre = tail
            head = tail.next

        return dummy.next

    def reverse(self, head, tail):
        pre = None
        cur = head
        while pre != tail:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return tail, head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        tail = head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next 
        
        newHead = self.reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)

        return newHead
        

    def reverse(self, head, tail):
        pre = None
        while head != tail:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ll = 0
        cur = head
        while(cur):
            cur = cur.next
            ll += 1
        
        times = ll // k
        dummy = ListNode(-1, head)
        pre = dummy
        cur = head
        for _ in range(times):
            for _ in range(0, k-1):
                nxt = cur.next
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
            pre = cur
            cur = pre.next
        return dummy.next
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
