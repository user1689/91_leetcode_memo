
## 题目
https://leetcode-cn.com/problems/h-index/

## 思路
sort+binarySearch, countSort

```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # simplify
        # binarySearch -> 一次遍历
        def Num(target):
            ans = 0
            for numC in citations:
                if (numC >= target):
                    ans += 1
            return ans >= target

        # time nlogn
        # space 1
        citations.sort()
        
        leftH, rightH = 0, len(citations)
        while (leftH < rightH):
            mid = leftH + (rightH - leftH + 1) // 2
            if Num(mid):
                leftH = mid
            else:
                rightH = mid - 1
        return leftH
                
#  0 1 2 3 4 5 
#  1 1 1 1 0 0    

#  4 - 3 + 1 = 2
#  0 1 2
# [0 1 3 5 6]
#  0 0 0 1 1

```

## 复杂度分析
* time nlogn
* space 1

## 相关题目
1. 待补充
