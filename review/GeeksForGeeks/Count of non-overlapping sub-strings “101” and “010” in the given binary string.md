## 题目
https://www.geeksforgeeks.org/count-of-non-overlapping-sub-strings-101-and-010-in-the-given-binary-string/

## python3
```python3
class solution:
    def countSubStr(self, s: str):
        i = 0
        n = len(s)
        cnt = 0
        while (i < n - 2): 
            if (s[i] == '1' and s[i + 1] == '0' and  s[i + 2] == '1'):
                cnt += 1
                i += 3
            elif (s[i] == '0' and s[i + 1] == '1' and  s[i + 2] == '0'):
                cnt += 1
                i += 3
            else:
                i += 1
        return cnt

obj = solution()
s = "10101010101"
res = obj.countSubStr(s)
print(res)
```
