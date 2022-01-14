## 题目
https://leetcode-cn.com/problems/multiply-strings/

## 思路
imitation

## python3
```python3
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def addTwoNum(ans, curr):
            add = 0
            res = []
            i, j = len(ans) - 1, len(curr) - 1
            while (i >= 0 or j >= 0 or add != 0):
                tmp1 = int(ans[i]) if i >= 0 else 0
                tmp2 = int(curr[j]) if j >= 0 else 0
                result = tmp1 + tmp2 + add
                res.append(str(result % 10))
                add = result // 10
                i -= 1
                j -= 1
            return "".join(res[::-1])

        ans = "0"
        n, m = len(num1), len(num2)
        # 枚举digit
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num1[i])
            curr = ["0"] * (n - i - 1)
            # 与另一个num相乘
            for j in range(m - 1, -1, -1):
                tmp = int(num2[j]) * y + add
                curr.append(str(tmp % 10))
                add = tmp // 10
            if (add > 0):
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = addTwoNum(ans, curr)
        return ans     
```

## 复杂度分析
* time n * m + n**2
* space n

## 相关题目
1. 待补充
