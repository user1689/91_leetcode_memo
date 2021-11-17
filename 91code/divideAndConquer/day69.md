## 题目
https://leetcode-cn.com/problems/merge-k-sorted-lists/

## 思路
divideAndConquer, Heap

## python3
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def divide(low, high):
            if low == high:
                return lists[low]
            mid = low + (high - low) // 2
            leftNode = divide(low, mid)
            rightNode = divide(mid + 1, high)
            return merge(leftNode, rightNode)
        
        def merge(leftNode, rightNode):
            if not leftNode:
                return rightNode
            if not rightNode:
                return leftNode
            if leftNode.val < rightNode.val:
                leftNode.next = merge(leftNode.next, rightNode)
                return leftNode
            else:
                rightNode.next = merge(leftNode, rightNode.next)
                return rightNode
        
        if not lists:
            return None
        return divide(0, len(lists) - 1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        # time nlogn
        # space n
        # heapq
        # 遍历lists加入所有node的值 python默认最小堆直接弹出后串起来即可
        heap = []
        for node in lists:
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        dummy = ListNode(0, None)
        cur = dummy
        while heap:
            Val = heapq.heappop(heap)
            cur.next = ListNode(Val, None)
            cur = cur.next
        return dummy.next
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. https://leetcode-cn.com/problems/merge-two-sorted-lists/
2. https://leetcode-cn.com/problems/merge-sorted-array/
