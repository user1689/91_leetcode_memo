## 题目
https://leetcode-cn.com/problems/insert-interval/

## 思路
imitation

## python3
```python3
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        res = []
        placed = False
        for i in range(0, len(intervals)):
            leftTmp, rightTmp = intervals[i]
            # 不需要插入条件
            if (rightTmp < left):
                res.append([leftTmp, rightTmp])
            # 结束插入的条件
            elif (right < leftTmp):
                # 对插入进行分类
                if (not placed):
                    res.append([left, right])
                    placed = True
                res.append([leftTmp, rightTmp])
            # 需要插入的情况
            else:
                left = min(leftTmp, left)
                right = max(rightTmp, right)
        if not placed:
            res.append([left, right])
        return res
```
## 复杂度分析
* time n 
* space n

## 相关题目
1. 待补充
