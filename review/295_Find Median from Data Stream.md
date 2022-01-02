## 题目
https://leetcode-cn.com/problems/find-median-from-data-stream/

## 思路
priorityQueue

## python3
```python3
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if (len(self.left) == 0 or num <= self.left[0][1]):
            heapq.heappush(self.left, (-num, num))
            if (len(self.left) - len(self.right) > 1):
                elementFromLeft = heapq.heappop(self.left)[1]
                heapq.heappush(self.right, elementFromLeft)
        else:
            heapq.heappush(self.right, num)
            if (len(self.right) > len(self.left)):
                elementFromRight = heapq.heappop(self.right)
                heapq.heappush(self.left, (-elementFromRight, elementFromRight))

    def findMedian(self) -> float:
        if ((len(self.left) + len(self.right)) % 2 == 0):
            return (self.left[0][1] + self.right[0]) / 2
        else:
            return self.left[0][1]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. 待补充
