# 题目
https://leetcode-cn.com/problems/intersection-of-two-linked-lists/

# 思路
两次遍历

# python
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
            if curB:
                curB = curB.next
            else:
                curB = headA
        return curA
```

# 时间复杂度
* time n
* space 1

# 相关题目
1. https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/
