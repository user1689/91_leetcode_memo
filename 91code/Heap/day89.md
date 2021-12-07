## 题目
https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/

## 思路
Heap, BinarySearch

## python3
```python3
# Heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))

        while(heap):
            val, x, y = heapq.heappop(heap)
            k -= 1
            if k == 0:
                return val
            if (y < n - 1):
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
# BinarySearch
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def check(mid):
            i = n - 1
            j = 0
            count = 0
            while i >= 0 and j < n:
                if (matrix[i][j] <= mid):
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count >= k

        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while (left < right):
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

```

## 复杂度分析
* time log(r-l)
* space 1

## 相关题目
1. 待补充
