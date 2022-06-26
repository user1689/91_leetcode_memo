# [1371\. Find the Longest Substring Containing Vowels in Even Counts](https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/)

## Description

Difficulty: **中等**  

Related Topics: [Bit Manipulation](https://leetcode.cn/tag/bit-manipulation/), [Hash Table](https://leetcode.cn/tag/hash-table/), [String](https://leetcode.cn/tag/string/), [Prefix Sum](https://leetcode.cn/tag/prefix-sum/)


Given the string `s`, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

**Example 1:**

```
Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
```

**Example 2:**

```
Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
```

**Example 3:**

```
Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.
```

**Constraints:**

*   `1 <= s.length <= 5 x 10^5`
*   `s` contains only lowercase English letters.


## Solution

Language: java

```java
class Solution {
    public int findTheLongestSubstring(String s) {
        int n = s.length();
        int res = 0, status = 0;
        int[] p = new int[1 << 5];
        Arrays.fill(p, -1);
        p[0] = 0;
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == 'a') {
                status ^= (1 << 0);
            } else if (c == 'e') {
                status ^= (1 << 1);
            } else if (c == 'i') {
                status ^= (1 << 2);
            } else if (c == 'o') {
                status ^= (1 << 3);
            } else if (c == 'u') {
                status ^= (1 << 4);
            }
            if (p[status] >= 0) {
                res = Math.max(res, i - p[status] + 1);
            } else {
                p[status] = i + 1;
            }
        }
        return res;
    }
}
```
