# [202\. Happy Number](https://leetcode.cn/problems/happy-number/)

## Description

Difficulty: **简单**  

Related Topics: [Hash Table](https://leetcode.cn/tag/hash-table/), [Math](https://leetcode.cn/tag/math/), [Two Pointers](https://leetcode.cn/tag/two-pointers/)


Write an algorithm to determine if a number `n` is happy.

A **happy number** is a number defined by the following process:

*   Starting with any positive integer, replace the number by the sum of the squares of its digits.
*   Repeat the process until the number equals 1 (where it will stay), or it **loops endlessly in a cycle** which does not include 1.
*   Those numbers for which this process **ends in 1** are happy.

Return `true` _if_ `n` _is a happy number, and_ `false` _if not_.

**Example 1:**

```
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

**Example 2:**

```
Input: n = 2
Output: false
```

**Constraints:**

*   1 <= n <= 2<sup>31</sup> - 1


## Solution

Language: Java

```java
class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = n;
        fast = getNext(n);
        while (slow != fast && fast != 1) {
            slow = getNext(slow);
            fast = getNext(getNext(fast));
        }
        return fast == 1;
    }
    
    public int getNext(int n) {
        int ans = 0;
        while (n > 0) {
            int digit = n % 10;
            ans += digit * digit;
            n /= 10;
        }
        return ans;
    }
}
```
