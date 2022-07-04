# [395\. Longest Substring with At Least K Repeating Characters](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/)

## Description

Difficulty: **中等**  

Related Topics: [Hash Table](https://leetcode.cn/tag/hash-table/), [String](https://leetcode.cn/tag/string/), [Divide and Conquer](https://leetcode.cn/tag/divide-and-conquer/), [Sliding Window](https://leetcode.cn/tag/sliding-window/)


Given a string `s` and an integer `k`, return _the length of the longest substring of_ `s` _such that the frequency of each character in this substring is greater than or equal to_ `k`.

**Example 1:**

```
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
```

**Example 2:**

```
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

**Constraints:**

*   1 <= s.length <= 10<sup>4</sup>
*   `s` consists of only lowercase English letters.
*   1 <= k <= 10<sup>5</sup>


## Solution

Language: Java

```java
class Solution {
    public int longestSubstring(String s, int k) {
        int[] cnt = new int[26];
        int n = s.length();
        int ans = 0;
        for (int p = 1; p < 27; p++) {
            Arrays.fill(cnt, 0);
            int i = 0, j = 0;
            // tot: total english letters, sum: The total number of English letters whose quantity meets k
            int tot = 0, sum = 0;
            while (j < n) {
                int u = s.charAt(j) - 'a';
                cnt[u]++;
                if (cnt[u] == 1) tot++;
                if (cnt[u] == k) sum++;
                while (tot > p) {
                    int t = s.charAt(i) - 'a';
                    cnt[t]--;
                    if (cnt[t] == 0) tot--; 
                    if (cnt[t] == k - 1) sum--;
                    i++;
                }
                if (tot == sum) ans = Math.max(ans, j - i + 1);
                j++;
            }
        }
        return ans;
    }
}
```
