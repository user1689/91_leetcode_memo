## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
Moore

## python3
```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        # time n
        # space 1
        # 摩尔投票法
        element1 = 0
        element2 = 0
        vote1 = 0
        vote2 = 0
        for num in nums:
            if vote1 > 0 and element1 == num:
                vote1 += 1
            elif vote2 > 0 and element2 == num:
                vote2 += 1
            elif vote1 == 0:
                element1 = num
                vote1 += 1
            elif vote2 == 0:
                element2 = num
                vote2 += 1
            # 如果三个元素均不相同，则相互抵消1次
            else:
                vote1 -= 1
                vote2 -= 1
        
        # 统计是否超过一半
        res = []
        n = len(nums)
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == element1:
                cnt1 += 1
            if num == element2:
                cnt2 += 1
        # corner case:[0, 0, 0]
        # 此时数据:
        # element1 = 0, vote1 = 3, cnt1 = 3
        # element2 = 0, vote2 = 0, cnt2 = 3
        if vote1 > 0 and cnt1 > (n // 3):
            res.append(element1)
        if vote2 > 0 and cnt2 > (n // 3):
            res.append(element2)
        return res
```


## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
