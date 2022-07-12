# [1477\. Find Two Non-overlapping Sub-arrays Each With Target Sum](https://leetcode.cn/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/)

## Description

Difficulty: **中等**  

Related Topics: [Array](https://leetcode.cn/tag/array/), [Hash Table](https://leetcode.cn/tag/hash-table/), [Binary Search](https://leetcode.cn/tag/binary-search/), [Dynamic Programming](https://leetcode.cn/tag/dynamic-programming/), [Sliding Window](https://leetcode.cn/tag/sliding-window/)


You are given an array of integers `arr` and an integer `target`.

You have to find **two non-overlapping sub-arrays** of `arr` each with a sum equal `target`. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is **minimum**.

Return _the minimum sum of the lengths_ of the two required sub-arrays, or return `-1` if you cannot find such two sub-arrays.

**Example 1:**

```
Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
```

**Example 2:**

```
Input: arr = [7,3,4,7], target = 7
Output: 2
Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.
```

**Example 3:**

```
Input: arr = [4,3,2,6,2,3,4], target = 6
Output: -1
Explanation: We have only one sub-array of sum = 6.
```

**Constraints:**

*   1 <= arr.length <= 10<sup>5</sup>
*   `1 <= arr[i] <= 1000`
*   1 <= target <= 10<sup>8</sup>


## Solution

Language: Java

```java
class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int N = 100010;
        int n = arr.length;
        // dp[i] represents the min length of subarry which sum equals target ends at index i.
        int[] dp = new int[n];
        Arrays.fill(dp, 0x3f3f3f3f);
        int l = 0, r = 0;
        int curSum = 0;
        int res = N;
        while (r < n) {
            curSum+=arr[r];
            
            while (l<=r && curSum>target) {
                curSum-=arr[l++];
            }
            
            // 如果加上arr[r]的新子数组无法找到一个curSum==target更新dp[r]，此时只能试着从前一个位置转移
            // 如果加上arr[r]的新子数组找到多个curSum==target更新了dp[r]，此时对比dp[r]和dp[r-1]哪一个更小
            
            // dp[i] = min(dp[i-1], update(dp[i]))
            if (curSum==target) {
                dp[r]=r-l+1;
                if(r!=0){
                    dp[r]=Math.min(dp[r], dp[r-1]);
                }
                if(l!=0){
                    res = Math.min(res, dp[l-1]+r-l+1);
                }
            } else {
                if(r!=0){
                    dp[r]=Math.min(dp[r], dp[r-1]);
                }
            }
            
            r++;
        }
        return res == N ? -1 : res;
    }
}
```
