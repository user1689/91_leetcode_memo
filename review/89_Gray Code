## 题目
https://leetcode-cn.com/problems/gray-code/

## 思路
tricky

## python3
```python3
class Solution:
    def grayCode(self, n: int) -> List[int]:
        # time n
        # space n
        res = [0]
        head = 1
        for j in range(n):
            for i in range(len(res) - 1, -1, -1):
                res.append(head + res[i])
            head <<= 1
        return res
```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
