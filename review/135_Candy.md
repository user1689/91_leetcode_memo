## 题目
https://leetcode-cn.com/problems/candy/

## 思路

## python3
```python3
class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        1 从左到右扫一遍 按要求分配
        2 从右到左扫一遍 按要求分配
        1和2的结果取最大值 使两个分配条件都得到满足
        '''
        left = [0] * len(ratings)
        for i in range(0, len(ratings)):
            if (i > 0 and ratings[i] > ratings[i - 1]):
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        right = [0] * len(ratings)
        for j in range(len(ratings) - 1, -1, -1):
            if (j < len(ratings) - 1 and ratings[j] > ratings[j + 1]):
                right[j] = right[j + 1] + 1
            else:
                right[j] = 1
        res = 0
        for k in range(0, len(ratings)):
            res += max(left[k], right[k])
        return res
```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
