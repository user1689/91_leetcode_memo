## 题目
https://leetcode-cn.com/problems/binary-watch/

## 思路
DFS(backTracking)

## python3
```python3
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # time n**2
        # space 1
        # bruteForce
        def countBit(num):
            count = 0
            while(num > 0):
                if(num & 1):
                    count += 1
                num >>= 1
            return count
        res = []
        for hour in range(0, 12):
            for minute in range(0, 60):
                countHour = countBit(hour)
                countMinute = countBit(minute)
                if (countHour + countMinute) == turnedOn:
                    res.append("%d:%02d" % (hour, minute))
        return res
        
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        # time C 10 num
        # space num
        # backtracking
        def dfs(remains, startIdx, mark):
            # base
            if (remains == 0):
                hour = 1 * mark[0] + 2 * mark[1] + 4 * mark[2] + 8 * mark[3]
                minute = 1 * mark[4] + 2 * mark[5] + 4 * mark[6] + 8 * mark[7] + 16 * mark[8] + 32 * mark[9]
                
                if (hour < 12 and minute < 60):
                    res.append("%d:%02d" %(hour, minute))
                    
                return 
            
            for i in range(startIdx, 10):
                mark[i] = 1
                dfs(remains - 1, i + 1, mark)
                mark[i] = 0

        mark = [0] * 10
        res = []
        dfs(turnedOn, 0, mark)
        return res
```

## 复杂度分析
* time C 10个数选turnedOn个
* space turnedOn 

## 相关题目
1. 待补充
