# [992\. Subarrays with K Different Integers](https://leetcode.cn/problems/subarrays-with-k-different-integers/)

## Description

Difficulty: **困难**  

Related Topics: [Array](https://leetcode.cn/tag/array/), [Hash Table](https://leetcode.cn/tag/hash-table/), [Counting](https://leetcode.cn/tag/counting/), [Sliding Window](https://leetcode.cn/tag/sliding-window/)


Given an integer array `nums` and an integer `k`, return _the number of **good subarrays** of_ `nums`.

A **good array** is an array where the number of different integers in that array is exactly `k`.

*   For example, `[1,2,3,1,2]` has `3` different integers: `1`, `2`, and `3`.

A **subarray** is a **contiguous** part of an array.

**Example 1:**

```
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
```

**Example 2:**

```
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
```

**Constraints:**

*   1 <= nums.length <= 2 * 10<sup>4</sup>
*   `1 <= nums[i], k <= nums.length`


## Solution

Language: Java

```Java
class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMostKDiff(nums, k) - atMostKDiff(nums, k - 1);
    }
    
    // 最多 k - 最多 k - 1 = 恰好 k
    public int atMostKDiff(int[] nums, int k) {
        int i = 0, j = 0;
        int n = nums.length;
        int res = 0, count = 0;
        int[] cnt = new int[20010];
        while (j < n) {
            cnt[nums[j]] += 1;
            if (cnt[nums[j]] == 1) { count++; }
            
            while (i <= j && count > k) {
                cnt[nums[i]] -= 1;
                if (cnt[nums[i]] == 0) { count--; }
                i++;
            }
​
            // System.out.println("i:"+i+"j:"+j);
            res += j - i;
            j++;
        }
        return res;
    }
}
​
/*
​
1 [1,2]
2 [2,1] [1,2,1]
3 [1,2] [1,2,1,2] [2,1,2] 
4 [2,3]
​
​
*/
                if (cnt[nums[i]] == 0) { count--; }
```
