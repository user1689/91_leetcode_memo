## 题目
https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/

## 思路
DFS

## python3
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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        '''
        大概思路是有
        但是实现上还是不流畅
        细节考虑不够 比如base就没想到当一个节点就返回就ok 这样就不用在函数内部再考虑边界问题
        '''
        def dfs(head):
            if (not head):
                return None
            # 只有一个节点就直接返回了
            elif not head.next:
                return TreeNode(head.val)

            # find mid
            prev = None
            slow = head
            fast = head
            while(fast != None and fast.next != None):
                prev = slow
                slow = slow.next
                fast = fast.next.next

            # 断开左边区间和mid的链接
            prev.next = None
            right_root = slow.next

            root = TreeNode(slow.val)
            root.left = dfs(head)
            root.right = dfs(right_root)

            return root
        
        return dfs(head)
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
