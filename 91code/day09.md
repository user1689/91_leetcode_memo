## 题目
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

## 思路
双指针

## python
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # time nlogn 每次找中点为n 递归次数logn
        # space logn 即树的高度
        # 思路一
        # 双指针
        
        # base
        if not head:
            return None
        elif not head.next:
            return TreeNode(head.val)
        
        # 找到中点
        pre = None
        slow, fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        # 建立并断开前后连接点
        root = TreeNode(slow.val)
        pre.next = None
        
        # 递归建立左右子树
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

```

## 复杂度分析
* time nlogn 每次找中点为n 递归次数logn
* space logn

## 相关题目
1. https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
