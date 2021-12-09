## 题目
https://leetcode-cn.com/problems/design-skiplist/

## 思路
SkipList

## python3
```python3
class Node:
    def __init__(self, val = 0):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:

    def __init__(self):
        left = [Node(-1) for _ in range(16)]
        right = [Node(20001) for _ in range(16)]
        for i in range(15):
            left[i].right = right[i]
            left[i].down = left[i + 1]
            right[i].down = right[i + 1]
        left[-1].right = right[-1]
        self.head = left[0]


    def search(self, target: int) -> bool:
        cur = self.head
        while cur:
            if cur.right.val > target:
                cur = cur.down
            elif cur.right.val < target:
                cur = cur.right
            else:
                return True
        return False

    def add(self, num: int) -> None:
        cur = self.head
        stack = []
        
        while cur:
            if cur.right.val >= num:
                stack.append(cur)
                cur = cur.down
            else:
                cur = cur.right
        pre = None

        while stack:
            cur = stack.pop()
            node = Node(num)
            node.right = cur.right
            cur.right = node
            if pre:
                node.down = pre
            pre = node
            if random.randint(0, 1):
                break

    def erase(self, num: int) -> bool:
        cur = self.head
        is_removed = False
        while cur:
            if cur.right.val >= num:
                if cur.right.val == num:
                    is_removed = True
                    cur.right = cur.right.right
                cur = cur.down
            else:
                cur = cur.right
        return is_removed


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
```

## 复杂度分析
* time logn
* space n

## 相关题目
1. 待补充
