# [978\. Longest Turbulent Subarray](https://leetcode.cn/problems/longest-turbulent-subarray/)

## Description

Difficulty: **中等**  

Related Topics: [Array](https://leetcode.cn/tag/array/), [Dynamic Programming](https://leetcode.cn/tag/dynamic-programming/), [Sliding Window](https://leetcode.cn/tag/sliding-window/)


Given an integer array `arr`, return _the length of a maximum size turbulent subarray of_ `arr`.

A subarray is **turbulent** if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray `[arr[i], arr[i + 1], ..., arr[j]]` of `arr` is said to be turbulent if and only if:

*   For `i <= k < j`:
    *   `arr[k] > arr[k + 1]` when `k` is odd, and
    *   `arr[k] < arr[k + 1]` when `k` is even.
*   Or, for `i <= k < j`:
    *   `arr[k] > arr[k + 1]` when `k` is even, and
    *   `arr[k] < arr[k + 1]` when `k` is odd.

**Example 1:**

```
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
```

**Example 2:**

```
Input: arr = [4,8,12,16]
Output: 2
```

**Example 3:**

```
Input: arr = [100]
Output: 1
```

**Constraints:**

*   1 <= arr.length <= 4 * 10<sup>4</sup>
*   0 <= arr[i] <= 10<sup>9</sup>


## Solution

Language: Java

```java
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int res = 1;
        int i = 0, j = 0;
        int n = arr.length;
        while (j < n - 1) {
            /*
                    i   j
            case1: [2,1,2,1] 
            case2: [1,2,1,1]
            
                      ij
            case3: [1,1,2]
                    0 1
            */
            if (i == j) {
                if (arr[i] == arr[i+1]) {
                    i++;
                }
                j++;
            } else {
                if (arr[j] < arr[j - 1] && arr[j] < arr[j + 1]) {
                    j++;
                } else if (arr[j] > arr[j - 1] && arr[j] > arr[j + 1]) {
                    j++; 
                } else {
                    i = j;
                }
            }
            res = Math.max(res, j - i + 1);
        }
        return res;
    }
}
```
