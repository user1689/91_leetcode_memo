## 题目
https://leetcode-cn.com/problems/copy-list-with-random-pointer/

## 思路
DFS, imitation

## python3
```python3
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        注意一个节点可能被多个其他节点指向，因此我们可能递归地多次尝试拷贝某个节点，为了防止重复拷贝，我们需要首先检查当前节点是否被拷贝过，如果已经拷贝过，我们可以直接从哈希表中取出拷贝后的节点的指针并返回即可
        '''
        dic = dict()
        def dfs(head):
            if not head:
                return 
            if (head not in dic):
                newNode = Node(head.val, None, None)
                dic[head] = newNode
                newNode.next = dfs(head.next)
                newNode.random = dfs(head.random)

            return dic[head]

        return dfs(head)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        每次都把p放回head开始从头遍历
        从新建新节点到新建随机节点再到分割链表一共三步
        '''
        # step 1 create newNode
        p = head
        while(p):
            newNode = Node(p.val, None, None)
            newNode.next = p.next
            p.next = newNode
            p = p.next.next
        # step 2 create RrandomNode
        p = head
        while(p):
            if (p.random):
                p.next.random = p.random.next
            p = p.next.next
        # step 3 divide two linkedlist
        dummy = Node(-1, None, None)
        cur = dummy
        p = head
        while(p):
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next
        return dummy.next

```
## 复杂度分析
* time n
* space 1 

## 相关题目
1.待补充
