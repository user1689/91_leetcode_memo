# [60\. Permutation Sequence](https://leetcode.cn/problems/permutation-sequence/)

## Description

Difficulty: **困难**  

Related Topics: [Recursion](https://leetcode.cn/tag/recursion/), [Math](https://leetcode.cn/tag/math/)


The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for `n = 3`:

1.  `"123"`
2.  `"132"`
3.  `"213"`
4.  `"231"`
5.  `"312"`
6.  `"321"`

Given `n` and `k`, return the k<sup>th</sup> permutation sequence.

**Example 1:**

```
Input: n = 3, k = 3
Output: "213"
```

**Example 2:**

```
Input: n = 4, k = 9
Output: "2314"
```

**Example 3:**

```
Input: n = 3, k = 1
Output: "123"
```

**Constraints:**

*   `1 <= n <= 9`
*   `1 <= k <= n!`


## Solution

Language: Java

```java
class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder sb = new StringBuilder();
        List<Integer> num = new ArrayList<>();
        
        int fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
            num.add(i);
        }
        
        k = k - 1;
        for (int i = 0; i < n; i++) {
            fact /= (n - i);
            int index = k / fact;
            sb.append(num.remove(index));
            k %= fact;
        }
        return sb.toString();
    }
}
```
