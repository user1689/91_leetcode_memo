## 题目
https://leetcode.cn/problems/maximum-width-ramp/

## 思路
Monotonic stack

## Python3
```python3

```
## Java
```java
class Solution {
    public int maxWidthRamp(int[] nums) {
        
        // 维护一个单调递减栈  递增栈没意义 因为前面的i位置和大小一定小于后面的j j就失去了被遍历的意义
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int i = 0;
        int n = nums.length;
        while (i < n) {
            if (stack.isEmpty() || nums[stack.peekLast()] > nums[i]) {
                stack.offerLast(i);
            }
            i++;
        }
        
        int res = 0;
        for (int j = n-1; j >= 0; j--) {
            while (!stack.isEmpty() && nums[stack.peekLast()] <= nums[j]) {
                res = Math.max(res, j - stack.pollLast());
            } 
        }
        return res;
        
    }
}
```

## 复杂度分析
* time O(N)
* space O(N)

## 相关题目
1. https://leetcode.cn/problems/longest-well-performing-interval/
