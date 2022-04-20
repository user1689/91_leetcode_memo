## 题目
https://leetcode-cn.com/problems/excel-sheet-column-title/

## 思路

## python3
```python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''

        "ZY"  ->  26*(26^1) + 25*(26^0)

        '''

        res = []
        while(columnNumber):
            # 为了完成偏移 使区间落在[0,25]
            columnNumber -= 1
            res.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(res[::-1])
```

## 复杂度分析
* time O(log26columnNumber)
* space 1

## 相关题目
1. 待补充
