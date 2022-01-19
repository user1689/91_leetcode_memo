## 题目
https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/

## 思路
多路归并

## python3
```python3
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 多路归并
        # time klogk
        # space k
        heap = []
        m = len(nums1)
        n = len(nums2)
        for i in range(0, min(k, m)):
            heapq.heappush(heap, [nums1[i] + nums2[0], i, 0])
        res = []
        while (heap and k > 0):
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if (j + 1 <= n - 1):
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], i, j + 1])
            k -= 1
        return res

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # time k**2 * klogk
        # space logk
        # heap
        heap = []
        # speed up
        # because nums1 and nums2 are ascending array, so ans must appear in first k elements of nums1 and first k elements of nums2.
        for i in range(0, min(len(nums1), k)):
            for j in range(0, min(len(nums2), k)):
                heapq.heappush(heap, (nums1[i] + nums2[j], nums1[i], nums2[j]))
        res = []
        while heap and k > 0:
            _, tmp1, tmp2 = heapq.heappop(heap)
            res.append([tmp1, tmp2])
            k -= 1
        return res          
```

## 复杂度分析
* time klogk
* space k

## 相关题目
1. https://leetcode-cn.com/problems/k-th-smallest-prime-fraction/
