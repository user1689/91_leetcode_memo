# [735\. Asteroid Collision](https://leetcode.cn/problems/asteroid-collision/)

## Description

Difficulty: **中等**  

Related Topics: [Stack](https://leetcode.cn/tag/stack/), [Array](https://leetcode.cn/tag/array/)


We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

**Example 1:**

```
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10\. The 5 and 10 never collide.
```

**Example 2:**

```
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
```

**Example 3:**

```
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5\. The 10 and -5 collide resulting in 10.
```

**Constraints:**

*   2 <= asteroids.length <= 10<sup>4</sup>
*   `-1000 <= asteroids[i] <= 1000`
*   `asteroids[i] != 0`


## Solution

Language: Java

```java
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < asteroids.length; i++) {
            boolean flag = true;
            if (!stack.isEmpty() && stack.peekLast() * asteroids[i] > 0) {
                stack.offerLast(asteroids[i]);
                continue;
            }
            
            if (asteroids[i] < 0) {
                if (!stack.isEmpty()) {
                   while (!stack.isEmpty() && stack.peekLast() > 0) {
                        if (stack.peekLast() < Math.abs(asteroids[i])) {
                            stack.pollLast();   
                        } else if (stack.peekLast() > Math.abs(asteroids[i])){
                            flag = false;
                            break;
                        } else if (stack.peekLast() == Math.abs(asteroids[i])) {
                            flag = false;
                            stack.pollLast();  
                            break;
                        }
                    } 
                    if (flag) {
                        stack.offerLast(asteroids[i]);
                    }
                    
                } else {
                    stack.offerLast(asteroids[i]);
                }
            } else {
                stack.offerLast(asteroids[i]);
            }
            
        }
        int[] res = new int[stack.size()];
        for (int j = 0; j < res.length; j++) {
            res[j] = stack.pollFirst();
        }
        return res;
    }
}
```
