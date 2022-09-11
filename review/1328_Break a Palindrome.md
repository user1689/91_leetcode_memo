## 题目
https://leetcode.cn/problems/break-a-palindrome/

## 思路
Imitation

## Java
```java
class Solution {
    public String breakPalindrome(String palindrome) { 
        // corner case: "aba"
        // if len of palindrome is odd, we can not directly changed letter in the center of string to break a palindrome.
        // so we can traverse half length of palindrome, group the case: length of s is odd and case: all letters is 'a' into same case, and handle it together.
        int n = palindrome.length();
        if (n < 2) return "";
        char[] c = palindrome.toCharArray();
        for (int i = 0; i < n / 2; i++) {
            if (c[i] != 'a') {
                c[i] = 'a';
                return String.valueOf(c);
            } 
        }
        c[n-1] = 'b';
        return String.valueOf(c);
    }
}
```
