## 题目
https://leetcode-cn.com/problems/decode-ways/

## 思路
recursive + memorization, dp

## python3
```python3
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        分为两种情况 
        第一种 仅从当前字符转移 (此时范围在1到9)
        第二种 从前两个字符转移 (此时范围只能在10到26)

        当s = "1"
        n = 1, range(1, 2)
        so, i = 1
        由于py3的特性 s[i-2] + s[i-1] = s[-1] + s[0] = 11 (合法)
        所以又触发了dp[i] = dp[i - 2]
        '''
        n = len(s)
        dp = [0] * (n + 1)
        # 空串长度也为1
        dp[0] = 1
        for i in range(1, n+1):
            if (s[i - 1] != '0'):
                dp[i] += dp[i-1]
            # corner case "1"
            if (i > 1 and 10<=int(s[i-2] + s[i-1])<=26):
                dp[i] += dp[i-2]
        return dp[-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache
        def dfs(tmp : str):
            if (len(tmp) == 0):
                return 1
            if (tmp[0] == '0'):
                return 0
            if (len(tmp) == 1):
                return 1
            
            w = dfs(tmp[1:])
            prefix = int(tmp[0:2])
            if (prefix <= 26):
                w += dfs(tmp[2:])
            
            return w
        
        return dfs(s)
```

## 复杂度分析
* time n
* space n

## 相关题目
1. 待补充
