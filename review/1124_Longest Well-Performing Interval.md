## 题目
https://leetcode.cn/problems/longest-well-performing-interval/

## 思路
preSum + monotonic Stack

## Java
```java
class Solution {
    public int longestWPI(int[] hours) {
        /*
        
        [1,1,-1,-1,-1,-1,1]
        [1,2,1,0,-1,-2,-1]
        
        */
        
        int n = hours.length;
        int[] tmp = new int[n];
        for (int j = 0; j < n; j++) {
            if (hours[j] > 8) {
                tmp[j] = 1;
            } else {
                tmp[j] = -1;
            }
        }
            
        int[] preSum = new int[n+1];
        for (int i = 0; i < n; i++) {
            preSum[i+1] = preSum[i] + tmp[i];
        }
        
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        int k = 0;
        while (k < preSum.length) {
            if (stack.isEmpty() || preSum[stack.peekLast()] > preSum[k]) {
                stack.offerLast(k);
            }
            k++;
        }
        
        // for (int x: preSum) {
        //     System.out.println(x);
        // }
        
        int res = 0;
        int t = preSum.length - 1;
        while (t >= 0) {
            while (!stack.isEmpty() && preSum[stack.peekLast()] < preSum[t]) {
                res = Math.max(res, t - stack.pollLast());
            }
            t--;
        }
        return res;
    }
}
```

## 复杂度分析
*time O(N)
*space O(N)

## 相关题目
1. 待补充
