## 题目
https://leetcode-cn.com/problems/middle-of-the-linked-list/

## 思路
快慢指针

## python
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 写法一
    def middleNode(self, head: ListNode) -> ListNode:
        
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 写法二
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        return slow.next
```

## 时间复杂度
* time n
* space n

## 相关题目
1. 待补充
