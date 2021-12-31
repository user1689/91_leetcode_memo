## 题目
https://leetcode-cn.com/problems/restore-ip-addresses/

## 思路
DFS(backTracking)

## python3
```python3
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # time 3**|seg_count| * |s|
        # space seg_count
        def isValid(s, start, end):
            if (start > end):
                return False
            if (start != end and s[start] == '0'):
                return False
            num = 0
            for i in range(start, end + 1):
                if (s[i] > '9' or s[i] < '0'):
                    return False
                num = num * 10 + (int(s[i]))
                if (num > 255):
                    return False
            return True
        
        def backTracking(s, startIdx, pointNum):
            # base
            if pointNum == 3:
                if isValid(s, startIdx, len(s) - 1):
                    res.append(s)
                    return 
            for i in range(startIdx, len(s)):
                if isValid(s, startIdx, i):
                    s = s[:i+1] + '.' + s[i+1:]
                    pointNum += 1
                    backTracking(s, i + 2, pointNum)
                    pointNum -= 1
                    s = s[:i+1] + s[i+2:]
                else:
                    break

        if len(s) > 12:
            return []
        res = []
        backTracking(s, 0, 0)
        return res
```

## 复杂度分析
* time 3**|seg_count| * |s|
* seg_count

## 相关题目
1. 待补充
