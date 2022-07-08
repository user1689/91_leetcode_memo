# [1234\. Replace the Substring for Balanced String](https://leetcode.cn/problems/replace-the-substring-for-balanced-string/)

## Description

Difficulty: **中等**  

Related Topics: [String](https://leetcode.cn/tag/string/), [Sliding Window](https://leetcode.cn/tag/sliding-window/)


You are given a string s of length `n` containing only four kinds of characters: `'Q'`, `'W'`, `'E'`, and `'R'`.

A string is said to be **balanced**if each of its characters appears `n / 4` times where `n` is the length of the string.

Return _the minimum length of the substring that can be replaced with **any** other string of the same length to make_ `s` _**balanced**_. If s is already **balanced**, return `0`.

**Example 1:**

```
Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
```

**Example 2:**

```
Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
```

**Example 3:**

```
Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
```

**Constraints:**

*   `n == s.length`
*   4 <= n <= 10<sup>5</sup>
*   `n` is a multiple of `4`.
*   `s` contains only `'Q'`, `'W'`, `'E'`, and `'R'`.


## Solution

Language: Java

```java
class Solution {
    public int balancedString(String s) {
        /*
        
        QQQWEQQEREQWEQQQ
        [    ]
        
        16/4=4
        Q:9
        E:4
        W:2
        R:1
        
        
        四个字母相同数量都小于m的时, 窗口内的任意替换都可以使其合法
        
        */
        int[] cnt = new int[26];
        for (int i = 0; i < s.length(); i++) {
            cnt[s.charAt(i) - 'A']++;
        }
        int m = s.length() / 4;
        if (cnt['Q' - 'A'] <= m && cnt['W' - 'A'] <= m && cnt['E' - 'A'] <= m && cnt['R' - 'A'] <= m) {
            return 0;
        }
        int res = Integer.MAX_VALUE;
        int left = 0, right = 0;
        while (right < s.length()) {
            cnt[s.charAt(right) - 'A']--;
            right++;
            
            while (left <= right && cnt['Q' - 'A'] <= m && cnt['W' - 'A'] <= m && cnt['E' - 'A'] <= m && cnt['R' - 'A'] <= m) {
                res = Math.min(res, right - left);
                cnt[s.charAt(left) - 'A']++;
                left++;
            }
        }
        return res;
    }
}
```
