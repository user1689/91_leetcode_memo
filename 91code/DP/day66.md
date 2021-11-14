## 题目
https://leetcode-cn.com/problems/non-overlapping-intervals/

## 思路
Greedy

## python3
```python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        count = 0
        i = 0
        while(i < len(intervals)):
            count += 1
            j = i + 1
            while (j < len(intervals) and intervals[j][0] < intervals[i][1]):
                j += 1
            i = j
        return len(intervals) - count
            

# Greedy 
# 1.Sweeping line / diff
# 2.Sort
#  sort by starting point => the minimum number of intervals to cover the whole
#  sort by ending point => the maximum number of intervals that are non-overlapping
# Dp
# 
```

## 复杂度分析
* time n**2
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/maximum-length-of-pair-chain/
