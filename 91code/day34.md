## 题目
https://leetcode-cn.com/problems/the-number-of-full-rounds-you-have-played/

## 思路
模拟+分类讨论，转化为分钟来算

## python3
```python3
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        
        # time n
        # space n
        # 思路一
        # 模拟+分类讨论
        
        startHour, startMinute = map(int, startTime.split(":"))
        endHour, endMinute = map(int, finishTime.split(":"))
        
        res = 0
        # 情况一 隔天的情况
        # case1 "20:19" -> "08:04"
        # case2 "20:21" -> "20:18"
        if (startHour > endHour) or (startHour == endHour and startMinute > endMinute):
            res += (23 - startHour + endHour) * 4
            res += (60 - startMinute) // 15
            res += endMinute // 15
        # 情况二 不隔天的情况
        else:
            res += (endHour - startHour - 1) * 4
            res += (60 - startMinute) // 15
            res += endMinute // 15

        return max(res, 0)
        
class Solution:
    import math
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        
        # time 1
        # space 1
        # 思路二
        # 转化成分钟
        startHour, startMinute = startTime.split(":")
        endHour, endMinute = finishTime.split(":")

        startTime = int(startHour) * 60 + int(startMinute)
        endTime = int(endHour) * 60 + int(endMinute)
        
        if startTime > endTime:
            endTime += 60 * 24
        
        newStartTime = math.ceil(startTime/15)
        newEndTime = endTime//15
        # print(newStartTime)
        # print(newEndTime)

        # corner case:
        # "00:47"
        # "00:57"
        return max(0, (newEndTime * 15 - newStartTime * 15) // 15)

    
        
```
## 时间复杂度
* time 1
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
