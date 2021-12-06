## 题目
https://leetcode-cn.com/problems/sort-characters-by-frequency/

## 思路
Heap

## python3
```python3
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        heap = []
        for key, value in dic.items():
            heapq.heappush(heap, (-value, key))
        ans = []
        while(heap):
            freq, char = heapq.heappop(heap)
            ans.append(-freq*char)
        return ''.join(ans)

```

## 复杂度分析
* time nlogn
* space n

## 相关题目
1. 待补充
