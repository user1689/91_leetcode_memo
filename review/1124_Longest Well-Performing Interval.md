## 题目
https://leetcode.cn/problems/longest-well-performing-interval/

## 思路
preSum + monotonic Stack, preSum + hashMap

## Java
```java
class Solution {
    public int longestWPI(int[] hours) {
        /*
        
                [-1,-2,-3,-4,-3,-2,-1,0,1,2,3,4,5,6,5,4,3,2,1,0,-1,-2,-3,-4]
element in map:   x  x  x  x          x x x x x x x                     
valid ans:                [   ]
                        [        ]
                    [               ]
                 [                    ]
                 [                      ]
                                            ...
                     [                                           ]
                        [                                           ] 
                            [                                          ]

        
        */
        
        int n = hours.length;
        int preSum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        int i = 0;
        int res = 0;
        while (i < n) {
            preSum += hours[i] > 8 ? 1 : -1;
            if (preSum > 0) {
                res = Math.max(res, i + 1);
            } else if (map.containsKey(preSum - 1)){
                res = Math.max(res, i - map.get(preSum - 1));
            }
            if (!map.containsKey(preSum)) {
                map.put(preSum, i);
            }
            i++;
        }
        return res;
        
        
    }
}

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
