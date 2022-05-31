## 题目
https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1/#

## python3
```python3
#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
                # write your code here

        if (k == 0):
            return 0
            
        if (k > len(s)):
            return -1

        ll = 0
        rr = 0
        n = len(s)
        ans = -1
        seen = dict()
        while (rr < n):
            while (ll < rr and len(seen) == k and (s[rr] not in seen)):
                seen[s[ll]] -= 1
                if (seen[s[ll]] == 0):
                    del seen[s[ll]]
                ll += 1
            
            seen[s[rr]] = seen.get(s[rr], 0) + 1
            if (len(seen) == k):
                ans = max(ans, rr - ll + 1)
            rr += 1
        return ans
```
