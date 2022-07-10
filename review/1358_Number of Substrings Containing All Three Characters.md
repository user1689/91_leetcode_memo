# [1358\. Number of Substrings Containing All Three Characters](https://leetcode.cn/problems/number-of-substrings-containing-all-three-characters/)

## Description

Difficulty: **中等**  

Related Topics: [Hash Table](https://leetcode.cn/tag/hash-table/), [String](https://leetcode.cn/tag/string/), [Sliding Window](https://leetcode.cn/tag/sliding-window/)


Given a string `s` consisting only of characters _a_, _b_ and _c_.

Return the number of substrings containing **at least** one occurrence of all these characters _a_, _b_ and _c_.

**Example 1:**

```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
```

**Example 2:**

```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
```

**Example 3:**

```
Input: s = "abc"
Output: 1
```

**Constraints:**

*   `3 <= s.length <= 5 x 10^4`
*   `s` only consists of _a_, _b_ or _c _characters.


## Solution

Language: Python

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 解法二 枚举左边界
        n = len(s)
        l, r = 0, 0
        res = 0
        cnt = [0 for _ in range(3)]
        while (r < n):
            cnt[ord(s[r]) - ord('a')]+=1
            while (l<=r and cnt[0] >= 1 and cnt[1] >=1 and cnt[2] >=1):
                res+=n-r
                cnt[ord(s[l]) - ord('a')]-=1
                l+=1   
            r+=1
        return res


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 解法二 枚举右边界 
        res = 0
        dic = {"a":-1, "b":-1, "c":-1}
        for i in range(0, len(s)):
            # 因为右边界是一个区间所以需要更新右边界的左边界 从而计算子数组数量
            dic[s[i]] = i
            tmp = min(dic.values())
            if (tmp != -1):
                res += tmp+1
            # eg:  
            #    abc [abc]
            #  L1,2,3  R
            # 一个R可以和L1,2,3分别组成一个满足要求的子数组 + 本身
        return res
```
