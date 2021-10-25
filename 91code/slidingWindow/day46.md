## 题目
76. Minimum Window Substring

# 思路
slidingWindow

## python3
```python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # time n
        # space n
        # slidingWindow 

        if len(s) < len(t): return ""

        # step1 construct a new hashMap for counting the char in t.
        need = collections.defaultdict(int)
        for i in range(len(t)):
            need[t[i]] += 1
        needCnt = len(t)
        left = 0
        res=(0,float('inf'))

        # step2 move sliding window on
        for right in range(0, len(s)):
            if need[s[right]] > 0:
                needCnt -= 1
            need[s[right]] -= 1

            if needCnt == 0:
                while True:
                    char = s[left]
                    # find the shortest window in this loop
                    if need[char] == 0:
                        break
                    need[char] += 1
                    left += 1
                # calculate length of the window
                if right - left < res[1] - res[0]:
                    res = (left, right)
                # move to the next window that does not meet the criteria
                # s = "ADO|BECODEBANC" -> "ADOB|ECODEBANC"
                # t = "ABC"
                need[s[left]] += 1
                needCnt += 1
                left += 1

        return '' if res[1]>len(s) else s[res[0]:res[1]+1]

```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/
2. https://leetcode-cn.com/problems/minimum-size-subarray-sum/
3. https://leetcode-cn.com/problems/sliding-window-maximum/
4. https://leetcode-cn.com/problems/permutation-in-string/
5. https://leetcode-cn.com/problems/smallest-range/
6. https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
