## 题目
https://leetcode-cn.com/problems/boats-to-save-people/

## 思路
Greedy

## python3
```python3
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # time nlogn
        # space 1
        people.sort()
        count = 0
        i, j = 0, len(people) - 1
        # 无论people奇数偶数
        # 当i==j时 最后一个人一定会被分一艘船 然后退出循环
        while(i <= j):
            # 最轻的人和最重的人搭配
            if people[i] + people[j] <= limit:
                count += 1
                i += 1
                j -= 1
            # 搭配不成功就只能放下最重的人
            else:
                count += 1
                j -= 1
        return count
     
```

## 复杂度分析
* time nlogn
* space 1

## 相关题目
1. 待补充
