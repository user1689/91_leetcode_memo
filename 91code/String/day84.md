## 题目
https://leetcode-cn.com/problems/implement-strstr/

## 思路
KMP

## Java
```Java
class Solution {
    public int strStr(String haystack, String needle) {

        if (needle.length() == 0)
            return 0;

        int i = 0, j = 0;

        int[] next = getNext(needle);

        while (i < haystack.length() && j < needle.length()) {

            if (haystack.charAt(i) == needle.charAt(j)) {

                i++;
                j++;
            } else {

                if (j > 0)
                    j = next[j - 1];
                else
                    i++;
            }

            if (j == needle.length())
                return i - j;
        }

        return -1;
    }

    public int[] getNext(String pattern) {

        int[] next = new int[pattern.length()];

        int j = 0;
        for (int i = 1; i < pattern.length(); i++) {

            if (pattern.charAt(i) == pattern.charAt(j))
                next[i] = ++j;
            else {

                while (j > 0 && pattern.charAt(j) != pattern.charAt(i))
                    j = next[j - 1];

                if (pattern.charAt(i) == pattern.charAt(j))
                    next[i] = ++j;
            }
        }

        return next;
    }
}
```

## 复杂度分析
* time  n + m
* space  1

## 相关题目
1. 待补充 
