## 题目
https://leetcode-cn.com/problems/top-k-frequent-elements/

## 思路
最小堆，快速选择

## python
```python3
class Solution:
    # 写法一
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:   
        # time n + nlogk
        # space n
        # 优先队列
        counter = Counter()
        for num in nums:
            counter[num] += 1

        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, (value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]
class Solution:
    # 写法二
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def counterNums(nums):
            count = dict()
            for num in nums:
                if num in count.keys():
                    count[num] += 1
                else:
                    count[num] = 0
            return count
        
        def swap(idx1, idx2):
            num_cnt[idx1], num_cnt[idx2] = num_cnt[idx2], num_cnt[idx1]
        
        def quickSort(num_cnt, k, low, high):
            pivot = random.randint(low, high)
            swap(pivot, low)
            base = num_cnt[low][1]
            i = low
            for j in range(low+1, high+1):
                # [bigger/partition/smaller]
                if num_cnt[j][1] > base:
                    swap(i+1, j)
                    i += 1
            swap(low, i)
            
            # the number of bigger elements is k
            # so the index of these elements is [0,k-1]
            if i >= k - 1:
                return num_cnt[:k]
            elif i > k - 1:
                return quickSort(num_cnt, k, low, i - 1)
            else:
                return quickSort(num_cnt, k, i + 1, high)

        count = counterNums(nums)
        num_cnt = list(count.items())
        topKs = quickSort(num_cnt, k, 0, len(num_cnt)-1)
        return [item[0] for item in topKs]
```
## 复杂度分析
* time nlogk (heap) n**2/n (quickSelect)
* space n (heap) n (quickSelect)
## 相关题目
1. https://leetcode-cn.com/problems/top-k-frequent-words/
2. https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
