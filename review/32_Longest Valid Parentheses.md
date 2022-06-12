## 题目
https://leetcode.cn/problems/longest-valid-parentheses/

## 思路
dp -> stack -> two pointers

## Java
```java
class Solution {
    public int longestValidParentheses(String s) {
        int left = 0;
        int right = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                right++;
            } else {
                left++;
            }
            if (left == right) {
                res = Math.max(res, left * 2);  
            } else if (right > left) {
                left = 0;
                right = 0;
            }
        }
        left = 0; 
        right = 0;
        for (int j = s.length() - 1; j >= 0; j--) {
            if (s.charAt(j) == '(') {
                left++;
            } else {
                right++;
            }
            
            if (left == right) {
                res = Math.max(res, left * 2);
            } else if (left > right) {
                left = 0;
                right = 0;
            }
        }
        return res;
    }
}
```

## 复杂度分析
*time O(N)
*space O(1)

## 相关题目
1. 待补充
