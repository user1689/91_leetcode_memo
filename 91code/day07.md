## 题目
https://leetcode-cn.com/problems/rotate-list/

## 思路
双指针

## python3
```python
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
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/rotate-array/
2. https://leetcode-cn.com/problems/split-linked-list-in-parts/

![](https://github.com/user1689/leetcode_memo/blob/main/91code/images/C07D224B-7AE6-44FB-8EC3-21872DC68284.jpeg)
