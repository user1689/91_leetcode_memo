## 题目
https://leetcode-cn.com/problems/implement-strstr/

## 思路
滚动哈希(RK)

## python3
```python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0
        hash_val = 0
        prime = 100000007
        target = 0
        
        for i in range(0, len(haystack)):
            if (i < len(needle)):
                hash_val = hash_val * 26 + (ord(haystack[i]) - ord("a"))
                hash_val %= prime
                target = target * 26 + (ord(needle[i]) - ord("a"))
                target %= prime
            else:
                hash_val = (
                     hash_val - (ord(haystack[i - len(needle)]) - ord("a")) * 26 ** (len(needle) - 1)
                     ) * 26 + (ord(haystack[i]) - ord("a"))
                hash_val %= prime
            if (i >= len(needle) - 1) and (hash_val == target):
                return i - len(needle) + 1
        return 0 if hash_val == target else -1
```

## 复杂度分析
* time n + m
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/longest-duplicate-substring/
2. https://leetcode-cn.com/problems/shortest-palindrome/
3. https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/
4. https://leetcode-cn.com/problems/longest-chunked-palindrome-decomposition/
5. https://leetcode-cn.com/problems/distinct-echo-substrings/
6. https://leetcode-cn.com/problems/longest-happy-prefix/
