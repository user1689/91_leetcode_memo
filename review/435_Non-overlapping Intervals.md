## 题目
https://leetcode-cn.com/problems/non-overlapping-intervals/

## 思路
sort+Greedy

## python3
```python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''

        [1,2]
          [2,3]
        [1,  3]
            [3,4]
       
        证明1
        排序以后 最早的结束的会最先出现 
        假设当前区间结束点为x 那么它留下的空白区域为[x:] 此时有另一个区间结束点为y并且x<y 那么它留下的空白区间为[y:]
        由于x<y 所以[y:] < [x:]
        留下的空间越大 那么删除就越少 因此可以贪心的得到结果

        证明2
        从局部来看 当区间重叠 保留局部内最早结束的区间 来避免影响后面的区间


        区间选点贪心点在于选区间内左还是右端 选右端 -> 覆盖更多的区间 -> 选择(每个区间内至少包含一个)较少的点来覆盖区间
        435的贪心点在于在两个区间重叠时选结束早的区间 -> 留给后面更多空间 -> 后面则可以删除更少的区间

        区间选点证明
        局部最优解 -> 全局最优解
        (若此区间不是第一个则都有前面的区间来进行局部判断) 对于区间中任意一段 可以选择其最右的端点 来覆盖更多的重叠区间 -> 全局最优解

        一些思考
        算出这些区间中最多有几个互不相交的区间 
        
                             每个区间内至少包含一个 选出的选择最少的点来覆盖所有区间 

        移除最少的点来覆盖所有区间 -> 用总区间 - 不重叠的区间数目 = 最小需要删除的数目

        覆盖更多的区间 会 留下更多的空间
        '''

        intervals.sort(key=lambda x: x[1])
        i = 0
        j = 0
        n = len(intervals)
        # 统计保留下来的区间
        cnt = 0
        while (i < n):
            j = i + 1
            while (j < n and intervals[j][0] < intervals[i][1]):
                j += 1
            cnt += 1    
            i = j
        return n - cnt

```

## 复杂度分析
* time O(NlogN)
* space O(1)

## 相关题目
1.https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/
