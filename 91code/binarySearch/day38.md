## 题目
https://leetcode-cn.com/problems/first-bad-version/

## 思路
二分区间

## python3
```python3
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        left, right = 1, n
        while (left < right):
            mid = left + (right - left) // 2
            # if method return true, it means we find a bad version.
            if isBadVersion(mid):
                #  L   M     R
                # [1,2,3,4,5,6]
                # 写right = mid, 
                # 当right收缩时 当mid位置元素是bad是不可能错过mid对应的值 即使bad一定存在[L,R]区间内
                # 作为对比写成[L,R-1]就可能不包含bad元素即不符合题意
                right = mid
            else:
                left = mid + 1
        return right

        
```

## 时间复杂度
* time long
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
2. https://leetcode-cn.com/problems/search-insert-position/
3. https://leetcode-cn.com/problems/guess-number-higher-or-lower/
