# [678\. Valid Parenthesis String](https://leetcode.cn/problems/valid-parenthesis-string/)

## Description

Difficulty: **中等**  

Related Topics: [Stack](https://leetcode.cn/tag/stack/), [Greedy](https://leetcode.cn/tag/greedy/), [String](https://leetcode.cn/tag/string/), [Dynamic Programming](https://leetcode.cn/tag/dynamic-programming/)


Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` _if_ `s` _is **valid**_.

The following rules define a **valid** string:

*   Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
*   Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
*   Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
*   `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "(*)"
Output: true
```

**Example 3:**

```
Input: s = "(*))"
Output: true
```

**Constraints:**

*   `1 <= s.length <= 100`
*   `s[i]` is `'('`, `')'` or `'*'`.


## Solution

Language: Java

```java
class Solution {
    public boolean checkValidString(String s) {
        /*
        
        (() 
        *
        
        */
        
        Deque<Integer> stars = new ArrayDeque<>();
        Deque<Integer> parenthesis = new ArrayDeque<>();
        char[] c = s.toCharArray();
        
        for (int i = 0; i < c.length; i++) {
            if (c[i] == '*') {
                stars.offerLast(i);
            } else if (c[i] == '(') {
                parenthesis.offerLast(i);
            } else if (c[i] == ')') {
                
                if (!parenthesis.isEmpty()) {
                    parenthesis.pollLast();
                } else if (!stars.isEmpty()) {
                    stars.pollLast();
                } else {
                    return false;
                }
            }
            
        }
        
        while (!parenthesis.isEmpty()) {
            
            if (stars.isEmpty()) {
                return false;
            } else if (stars.peekLast() < parenthesis.peekLast()) {
                return false;
            } else {
                stars.pollLast();
                parenthesis.pollLast();
            }
            
        }
        return true;
    }
}
```
