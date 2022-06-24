## 题目
https://www.geeksforgeeks.org/longest-sub-array-sum-k/

## Java
```java
public class Solution {
    /**
     * @param nums: an array
     * @param k: a target value
     * @return: the maximum length of a subarray that sums to k
     */
    public int maxSubArrayLen(int[] nums, int k) {
        // Write your code here

        // b - a = k -> a = b - k
        // map -> if b - k in map.keys():

        int res = 0, preSum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for (int i = 0; i < nums.length; i++) {
            preSum += nums[i];
            if (map.containsKey(preSum - k)) {
                res = Math.max(res, i - map.get(preSum - k));
            }  
            map.putIfAbsent(preSum, i);
 
        }
        return res;
    }   
}
```

## 时间复杂度
* time O(N)
* space O(N)

## 相关题目
1. 待补充
