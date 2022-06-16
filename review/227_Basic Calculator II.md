# [227\. Basic Calculator II](https://leetcode.cn/problems/basic-calculator-ii/)

## Description

Difficulty: **中等**  

Related Topics: [Stack](https://leetcode.cn/tag/stack/), [Math](https://leetcode.cn/tag/math/), [String](https://leetcode.cn/tag/string/)


Given a string `s` which represents an expression, _evaluate this expression and return its value_. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2<sup>31</sup>, 2<sup>31</sup> - 1].

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

**Example 1:**

```
Input: s = "3+2*2"
Output: 7
```

**Example 2:**

```
Input: s = " 3/2 "
Output: 1
```

**Example 3:**

```
Input: s = " 3+5 / 2 "
Output: 5
```

**Constraints:**

*   1 <= s.length <= 3 * 10<sup>5</sup>
*   `s` consists of integers and operators `('+', '-', '*', '/')` separated by some number of spaces.
*   `s` represents **a valid expression**.
*   All the integers in the expression are non-negative integers in the range [0, 2<sup>31</sup> - 1].
*   The answer is **guaranteed** to fit in a **32-bit integer**.


## Solution

Language: Java

```java
class Solution {
    
    public static Map<Character, Integer> map = new HashMap<>() {
    {
        put('+', 1);
        put('-', 1);
        put('*', 2);
        put('/', 2);
    }
    };
    
    public void calc(Deque<Integer> nums, Deque<Character> ops) {
        if (nums.isEmpty() || ops.isEmpty() || nums.size() < 2) {
            return ;
        }
        int num2 = nums.pollLast();
        int num1 = nums.pollLast();
        char op = ops.pollLast();
        int res = 0;
        if (op == '+') {
            res = num1 + num2; 
        } else if (op == '-') {
            res = num1 - num2;
        } else if (op == '*') {
            res = num1 * num2;
        } else if (op == '/') {
            res = num1 / num2;
        }
        nums.offerLast(res);
    }
    
    public int calculate(String s) {
        /*
        
        
        3+1-2*2+1-3/2-2
        
        
        [3 1]
        [+] - 
        
        
        */
        
        Deque<Integer> nums = new ArrayDeque<>();
        Deque<Character> ops = new ArrayDeque<>();  
        s = '0' + s;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == ' ') continue;
            if (Character.isDigit(c)) {
                int num = 0;
                while (i < s.length() && Character.isDigit(s.charAt(i))) {
                    num = num * 10 + (s.charAt(i) - '0');
                    i++;
                }
                nums.offerLast(num);
                i--;
            } else {
                while (!ops.isEmpty() && map.get(ops.peekLast()) >= map.get(c)) {
                    calc(nums, ops);
                }
                ops.offerLast(c);
            }
        }
        while (!ops.isEmpty()) {
            calc(nums, ops);
        }
        return nums.peekLast();
    }
}
```
