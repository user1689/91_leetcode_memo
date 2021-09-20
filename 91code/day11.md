# 题目
https://leetcode-cn.com/problems/linked-list-cycle-ii/

# 思路
哈希集合, 双指针

# python
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # time n
        # space 1

        # 推导1
        # P1 = D + s1
        # P2 = D + n(s1 + s2) + s1
        # 2(D + s1) = D + n(s1 + s2) + s1
        # 推导公式 D = (n - 1)(s1 + s2) + s2
        
        fast = head
        slow = head
        # 开始进入环
        while True:
            if not fast or not fast.next:
                return 
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        # 退出循环此时slow和fast相遇
        # 因为z和x相等，再走slow指针z步即可和从head重新出发走了x步的fast相遇与环入口
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

```
# 复杂度分析
* time n
* space 1

# 相关题目
1. https://leetcode-cn.com/problems/linked-list-cycle/
