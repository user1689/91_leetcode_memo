 # [385\. Mini Parser](https://leetcode.cn/problems/mini-parser/)

## Description

Difficulty: **中等**  

Related Topics: [Stack](https://leetcode.cn/tag/stack/), [Depth-First Search](https://leetcode.cn/tag/depth-first-search/), [String](https://leetcode.cn/tag/string/)


Given a string s represents the serialization of a nested list, implement a parser to deserialize it and return _the deserialized_ `NestedInteger`.

Each element is either an integer or a list whose elements may also be integers or other lists.

**Example 1:**

```
Input: s = "324"
Output: 324
Explanation: You should return a NestedInteger object which contains a single integer 324.
```

**Example 2:**

```
Input: s = "[123,[456,[789]]]"
Output: [123,[456,[789]]]
Explanation: Return a NestedInteger object containing a nested list with 2 elements:
1\. An integer containing value 123.
2\. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789
```

**Constraints:**

*   1 <= s.length <= 5 * 10<sup>4</sup>
*   `s` consists of digits, square brackets `"[]"`, negative sign `'-'`, and commas `','`.
*   `s` is the serialization of valid `NestedInteger`.
*   All the values in the input are in the range [-10<sup>6</sup>, 10<sup>6</sup>].


## Solution

Language: Java

```java
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public NestedInteger deserialize(String s) {
        /*
        
        从前往后遍历 遇到[就进入说明需要入栈了 遇到`,`或者`]`的话再进行分类讨论
        
        
        */
        if (s.charAt(0) != '[') {
            return new NestedInteger(Integer.parseInt(s));
        }
        ArrayDeque<NestedInteger> stack = new ArrayDeque<>();
        int n = s.length();
        int i = 0;
        boolean isNeg = false;
        int num = 0;
        while (i < n) {
            if (s.charAt(i) == '-') {
                isNeg = true;
            } else if (s.charAt(i) == '[') {
```
