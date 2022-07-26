# [522\. Longest Uncommon Subsequence II](https://leetcode.cn/problems/longest-uncommon-subsequence-ii/)

## Description

Difficulty: **中等**  

Related Topics: [Array](https://leetcode.cn/tag/array/), [Hash Table](https://leetcode.cn/tag/hash-table/), [Two Pointers](https://leetcode.cn/tag/two-pointers/), [String](https://leetcode.cn/tag/string/), [Sorting](https://leetcode.cn/tag/sorting/)


Given an array of strings `strs`, return _the length of the **longest uncommon subsequence** between them_. If the longest uncommon subsequence does not exist, return `-1`.

An **uncommon subsequence** between an array of strings is a string that is a **subsequence of one string but not the others**.

A **subsequence** of a string `s` is a string that can be obtained after deleting any number of characters from `s`.

*   For example, `"abc"` is a subsequence of `"aebdc"` because you can delete the underlined characters in `"a<u>e</u>b<u>d</u>c"` to get `"abc"`. Other subsequences of `"aebdc"` include `"aebdc"`, `"aeb"`, and `""` (empty string).

**Example 1:**

```
Input: strs = ["aba","cdc","eae"]
Output: 3
```

**Example 2:**

```
Input: strs = ["aaa","aaa","aa"]
Output: -1
```

**Constraints:**

*   `2 <= strs.length <= 50`
*   `1 <= strs[i].length <= 10`
*   `strs[i]` consists of lowercase English letters.


## Solution

Language: java

```Java
class Solution {
    public int findLUSlength(String[] strs) {
        int ans = -1;
        int n = strs.length;
        for (int i = 0; i < n; i++) {
            boolean flag = true;
            for (int j = 0; j < n; j++) {
                if (j != i && isSubsequence(strs[i], strs[j])) {
                    flag = false;
                    break;
                }
            }
            // System.out.println(flag);
            if (flag) {
                ans = Math.max(ans, strs[i].length());
            }
        }
        return ans;
        
    }
    public boolean isSubsequence(String s1, String s2) {
        int i = 0, j = 0;
        while (i < s1.length() && j < s2.length()) {
            if (s1.charAt(i) == s2.charAt(j)) {
                i++;
            }
            j++;
        }
        return i == s1.length() ? true : false;
    }
}
```
