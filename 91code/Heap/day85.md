## 题目
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

## 思路
Heap, quickSelection

## python3
```python3
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time nlogk
        # space logn
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        for _ in range(k):
            tmp = heapq.heappop(heap)
        return -tmp

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # time nlogk
        # space logn
        # 维护一个大小为k的最小堆，堆顶是这k个数里的最小的，遍历完数组后返回堆顶元素即可
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# [1, 2, 3, 4, 5 ,6], k = 2
# [5, 6]

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(low, high):
            # conercase:
            # [1,2,3,4,5,6]
            # [6,5,4,3,2,1]
            pivot = random.randint(low, high)
            nums[pivot], nums[low] = nums[low], nums[pivot]
            i, j = low, low + 1
            while j <= high:
                if nums[j] > nums[low]:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[low], nums[i] = nums[i], nums[low]
            return i
        
        def quickSort(low, high):
            while True:
                # [  ] idx==k-1 [  ]
                # 6 5 4 3 2 1
                # 0 1 2 3 4 5
                # 2thLargest:idx=2-1=1
                idx = partition(low, high)
                if idx == k - 1:
                    return nums[idx]
                elif idx < k - 1:
                    # return partition(idx + 1, high)
                    low = idx + 1
                elif idx > k - 1:
                    # return partition(low, idx - 1)
                    high = idx - 1
        
        return quickSort(0, len(nums) - 1)
        # return nums
```

## 复杂度分析
* time n
* space logn

## 相关题目
1. 待补充
