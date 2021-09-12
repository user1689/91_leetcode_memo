## 题目
https://leetcode-cn.com/problems/design-a-stack-with-increment-operation/
## 思路
* 思路一brute force
* 思路二前缀和优化

## python
```python
# 思路一
class CustomStack:
    # time n
    # space n
    def __init__(self, maxSize: int):
        self.stack = list()
        self.maxSize = maxSize
        self.size = 0

    def push(self, x: int) -> None:
        if self.size == self.maxSize:
            return
        else:
            self.size += 1
            self.stack.append(x)
            
    def pop(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if self.size <= k:
            for i in range(0, self.size):
                self.stack[i] += val
        else:
            for i in range(0, k):
                self.stack[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

# 思路二
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = list()
        self.maxSize = maxSize
        self.size = 0
        self.increments = list()

    def push(self, x: int) -> None:
        if self.size == self.maxSize:
            return
        else:
            self.size += 1
            self.stack.append(x)
            # 加0备用
            self.increments.append(0)
            
    def pop(self) -> int:
        if self.size == 0:
            return -1
        self.size -= 1
        # 由于先减size 所以当长度为2时 判断却size为1，但此时还是需要进行转移的
        # 所以选择使用>=1
        if self.size >= 1:
            self.increments[-2] += self.increments[-1]
        return self.stack.pop() + self.increments.pop()
        
    def increment(self, k: int, val: int) -> None:
        # 如果存在 
        if self.increments:
            # 底层k个元素增1即为 index为 0 到 (k -1)的元素
            # 为了符合题意(k - 1)与size取小
            # += 是为了当多次调用increment时 值不会被覆盖
            self.increments[min(k - 1, self.size - 1)] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
```

## 复杂度分析
* time 1
* space n

## 相关题目
1. 待补充
