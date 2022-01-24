## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
binarySearch

## python3
```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 二分左界
        n = len(citations)
        if citations[n - 1] == 0:
            return 0
        left, right = 0, n - 1
        while(left < right):
            mid = left + (right - left) // 2
            if (citations[mid] < n - mid):
                left = mid + 1
            else:
                right = mid
        return n - left
        
# reference
# https://leetcode-cn.com/problems/h-index-ii/solution/jian-er-zhi-zhi-er-fen-cha-zhao-by-liweiwei1419-2/
# https://leetcode-cn.com/problems/h-index-ii/solution/er-fen-xia-biao-ji-da-hua-hzhi-shu-by-23-m6b2/
```


## 复杂度分析
* time logn
* space 1

## 相关题目
1. 待补充
