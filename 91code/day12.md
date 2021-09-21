# 题目
https://leetcode-cn.com/problems/lru-cache/submissions/

# 思路
哈希表+双向链表

# python
```python3
class DListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    # time 1
    # space n
    # 思路一
    # 哈希表+双向链表

    # map查的快但是, 无法记录最近最久使用
    # arr删除只能做到O(n)因为得移动后面部分
    # linkedlist结合map 链表插入删除+哈希表查 但是链表进行删除有些麻烦访问前个元素
    # 所以使用双向链表(可以直接访问前个元素进行删除)+map

    def __init__(self, capacity: int):
        self.dic = dict()
        self.head = DListNode()
        self.tail = DListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        # 如果key不存在哈希表中直接返回-1
        if key not in self.dic:
            return -1
        # 如果存在 返回值 + 更新最新访问对象
        # 通过哈希表定位然后移动到头部
        node = self.dic[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # 如果不存在
        if key not in self.dic:
            node = DListNode(key, value)
            self.dic[key] = node
            self.addToHead(node)
            self.size += 1
            # 如果超出容量，删除双向链表的尾部节点
            if self.size > self.capacity:
                removed = self.removeTail()
                self.dic.pop(removed.key)
                self.size -= 1
        # 如果存在
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.dic[key]
            node.val = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        # 以node为基准
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToHead(self, node):
        # 以head为基准
        node.prev = self.head
        node.next = self.head.next
        # 此处注意连接顺序
        self.head.next.prev = node
        self.head.next = node
        
    def removeTail(self):
        # 获取末尾元素
        node = self.tail.prev
        # 移去末尾元素
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

# 复杂度分析
* time O(1)
* space O(n)

# 相关题目
1.https://leetcode-cn.com/problems/lfu-cache/
