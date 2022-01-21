## 题目
https://leetcode-cn.com/problems/rotate-list/

## 思路
imitation, fast and slow pointers

## python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time n
        # space 1
        cur = head
        count = 0
        while(cur != None):
            cur = cur.next
            count += 1
        
        # corner case:
        # []
        # 0
        # [1]
        # 0
        if (count == 0 or not head.next or not head):
            return head

        step = k % count
        # speed up
        if (step == 0):
            return head
        tmp = count - step
        dummy = ListNode(0, head)
        breakPoint = dummy
        while(tmp > 0):
            breakPoint = breakPoint.next
            tmp -= 1
        
        nxt = breakPoint.next 
        breakPoint.next = None
        tmp2 = nxt
        while(tmp2.next != None):
            tmp2 = tmp2.next
        tmp2.next = dummy.next
        return nxt

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # time n
        # space 1
        # 双指针
        if not head or not head.next: return head
        
        # 计算长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        # 对长度取模
        # 如果取余为0，则表示旋转后和原本相同，则不旋转直接返回
        k %= length
        if k == 0: return head

        dummy = ListNode(None, head)
        slow, fast = dummy, dummy
        while k > 0:
            fast = fast.next
            k -= 1
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        
        newHead = slow.next
        slow.next = None
        fast.next = dummy.next
        
        return newHead
```

## 复杂度分析
* time 
* space 

## 相关题目
1. https://leetcode-cn.com/problems/rotate-array/
2. https://leetcode-cn.com/problems/split-linked-list-in-parts/
