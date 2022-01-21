## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
sort

## python3
```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        for idx, interval in enumerate(intervals):  
            while (res and res[-1][1] >= interval[0]):
                left, right = res.pop()
                interval = [min(left, interval[0]), max(right, interval[1])]
            res.append(interval)
        return res     
```


## 复杂度分析
* time nlogn
* space n

## 相关题目
1. https://leetcode-cn.com/problems/insert-interval/
2. https://leetcode-cn.com/problems/teemo-attacking/
3. https://leetcode-cn.com/problems/partition-labels/
4. https://leetcode-cn.com/problems/interval-list-intersections/
