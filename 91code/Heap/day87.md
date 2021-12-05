## 题目
https://leetcode-cn.com/problems/merge-k-sorted-lists/

## 思路
Heap

## python3
```python3
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
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # time nlogn
        # space n
        heap = []
        # for i, node in enumerate(lists):
        #     if node:
        #         heapq.heappush(heap, (node.val, i))
        for i in range(0, len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))

        if not heap: return None
        dummy = ListNode(0, None)
        cur = dummy

        while heap:
            val, idx = heapq.heappop(heap)
            cur.next = ListNode(val, None)
            cur = cur.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heapq.heappush(heap, (lists[idx].val, idx))
        return dummy.next        
```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. 待补充
