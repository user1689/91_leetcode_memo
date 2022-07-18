# [324\. Wiggle Sort II](https://leetcode.cn/problems/wiggle-sort-ii/)

## Description

Difficulty: **中等**  

Related Topics: [Array](https://leetcode.cn/tag/array/), [Divide and Conquer](https://leetcode.cn/tag/divide-and-conquer/), [Quickselect](https://leetcode.cn/tag/quickselect/), [Sorting](https://leetcode.cn/tag/sorting/)


Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

You may assume the input array always has a valid answer.

**Example 1:**

```
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.
```

**Example 2:**

```
Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]
```

**Constraints:**

*   1 <= nums.length <= 5 * 10<sup>4</sup>
*   `0 <= nums[i] <= 5000`
*   It is guaranteed that there will be an answer for the given input `nums`.

**Follow Up:** Can you do it in `O(n)` time and/or **in-place** with `O(1)` extra space?

## Solution

Language: Java

```java
class Solution {
    public void wiggleSort(int[] nums) {
        // tip1 sort
        // tip2 traverse reversely
        // tip3 [4,5,5,6]
        int[] tmp = Arrays.copyOf(nums, nums.length);
        Arrays.sort(tmp);
        int i = (nums.length - 1) / 2, j = nums.length - 1;
        for (int k = 0; k < nums.length; k++) {
            // if k is odd, it should be a peek.
            if (k % 2 == 1) {
                nums[k] = tmp[j];
                j--;
            // if k is even, it should be a valley.
            } else if (k % 2 == 0) {
                nums[k] = tmp[i];
                i--;
            }
        }
        return;
    }
}
```
