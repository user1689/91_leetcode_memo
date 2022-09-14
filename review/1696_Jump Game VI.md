## 题目
https://leetcode.cn/problems/jump-game-vi/

## 思路

## java
```java
class Solution {
    public int maxResult(int[] nums, int k) {
        int n = nums.length;
        Deque<Integer> deque = new LinkedList();
        deque.offerLast(0);
        int[] f = new int[n];
        f[0] = nums[0];
        for(int i = 1; i < n; i++){
            while(!deque.isEmpty() && i - deque.peekFirst() > k)  deque.pollFirst();
            f[i] = f[deque.peekFirst()] + nums[i];
            while(!deque.isEmpty() && f[i] >= f[deque.peekLast()])  deque.pollLast();
            deque.offerLast(i);
        }
        return f[n - 1];
    }
}
```
## 复杂度分析

## 相关题目
