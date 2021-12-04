## 题目
https://leetcode-cn.com/problems/last-stone-weight/

## 思路
Heap

## python3
```python3
class heapq:
    def __init__(self, descend = False):
        self.heap = []
        self.descend = descend

    # @property
    def size(self):
        return len(self.heap)
    
    def top(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def push(self, val):
        '''
        存入末尾
        上浮
        '''
        self.heap.append(val)
        self._sift_up(self.size() - 1)
    
    def pop(self):
        '''
        存入tmp
        交换元素
        删除元素
        下沉
        返回tmp
        '''
        tmp = self.top()
        self._swap(0, self.size() - 1)
        self.heap.pop()
        self._sift_down(0)
        return tmp
    

    def _smaller(self, lst, rst):
        return lst > rst if self.descend else lst < rst


    def _swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]


    def _sift_up(self, idx):
        while idx != 0:
            parentIdx = (idx - 1) // 2

            if self._smaller(self.heap[parentIdx], self.heap[idx]):
                break
            
            self._swap(idx, parentIdx)
            idx = parentIdx

    def _sift_down(self, idx):
        while idx*2+1 < self.size():
            smallestIdx = idx
            leftIdx = idx*2+1
            rightIdx = idx*2+2

            if self._smaller(self.heap[leftIdx], self.heap[smallestIdx]):
                smallestIdx = leftIdx
            
            if rightIdx < self.size() and self._smaller(self.heap[rightIdx], self.heap[smallestIdx]):
                smallestIdx = rightIdx
            
            if smallestIdx == idx:
                break

            self._swap(idx, smallestIdx)
            idx = smallestIdx


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = heapq(descend=True)
        for stone in stones:
            heap.push(stone)
        # print(heap.size())
        while heap.size() > 1:
            weight1 = heap.pop()
            weight2 = heap.pop()
            if weight1 != weight2:
                remains = weight1 - weight2
                heap.push(remains)
        if heap.size() >= 1:
            return heap.top()
        return 0
```

## 复杂度分析
* time nlogn
* space logn

## 相关题目
1. 待补充
