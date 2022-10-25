# [772\. Basic Calculator III](https://leetcode.cn/problems/basic-calculator-iii/)

## Description

Difficulty: **困难**  

Related Topics: [Stack](https://leetcode.cn/tag/stack/), [Recursion](https://leetcode.cn/tag/recursion/), [Math](https://leetcode.cn/tag/math/), [String](https://leetcode.cn/tag/string/)


Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, `'+'`, `'-'`, `'*'`, `'/'` operators, and open `'('` and closing parentheses `')'`. The integer division should **truncate toward zero**.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2<sup>31</sup>, 2<sup>31</sup> - 1].

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

**Example 1:**

```
Input: s = "1+1"
Output: 2
```

**Example 2:**

```
Input: s = "6-4/2"
Output: 4
```

**Example 3:**

```
Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
```

**Constraints:**

*   1 <= s <= 10<sup>4</sup>
*   `s` consists of digits, `'+'`, `'-'`, `'*'`, `'/'`, `'('`, and `')'`.
*   `s` is a **valid** expression.


## Solution

Language: java

```java
public class Solution {
​
    public static Map<Character, Integer> map = new HashMap<>(){
        {
            put('+', 1);
            put('-', 1);
            put('*', 2);
            put('/', 2);
        }
    };
​
    public void calc(Deque<Integer> numStack, Deque<Character> opsStack) {
        if (numStack.isEmpty() || opsStack.isEmpty()) {
            return ;
        }
        int num1 = !numStack.isEmpty() ? numStack.pollLast() : 0; // divisor
        int num2 = !numStack.isEmpty() ? numStack.pollLast() : 0; // dividend
        char ops = opsStack.pollLast();
        int res = 0;
        switch(ops) {
            case('+'):
                res = num2 + num1;
                break;
            case('-'):
                res = num2 - num1;
                break;
            case('*'):
                res = num2 * num1;
                break;
            case('/'):
                res = num2 / num1;
                break;
        }
        // if (ops == '+') {
        //     res = num2 + num1; 
        // } else if (ops == '-') {
        //     res = num2 - num1;
        // } else if (ops == '*') {
        //     res = num2 * num1;
        // } else if (ops == '/') {
        //     res = num2 / num1;
        // }
        numStack.offerLast(res);
    }
​
    public int calculate(String s) {
        Deque<Integer> numStack = new ArrayDeque<>();
        Deque<Character> opsStack = new ArrayDeque<>();
        int n = s.length();
        numStack.offerLast(0);
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == ' ') continue;
            if (c == '+' || c == '-' || c == '*' || c == '/') {
                if (i > 0 && (s.charAt(i - 1) == '(' || s.charAt(i - 1) == '+' || s.charAt(i - 1) == '-')) {
                    numStack.offerLast(0);
                }
                while (!opsStack.isEmpty() && opsStack.peekLast() != '(' && map.get(opsStack.peekLast()) >= map.get(c)) {
                    calc(numStack, opsStack);
                }
                opsStack.offerLast(c); // add new operation
            } else if (c == '(') {
                opsStack.offerLast(c);
            } else if (c == ')') {
                while (!opsStack.isEmpty() && opsStack.peekLast() != '(') {
                    calc(numStack, opsStack);
                }
                opsStack.pollLast(); // remove (
```
