## topic
https://www.geeksforgeeks.org/printing-longest-common-subsequence/

## solution
```java
/*

Given two sequences, return the longest common subsequence (LCS) present in it. The LCS is the longest sequence which can be obtained from the first sequence by deleting some items and from the second sequence by deleting other items.

Input: X = "XMJYAUZ", Y = "MZJAWXU"
Output: "MJAU"

The longest common subsequence is not guaranteed to be unique. If multiple longest common subsequence exists, the solution should return any one of them.

Input: X = "ABCBDAB", Y = "BDCABA"
Output: "BDAB" or "BCAB" or "BCBA"

*/

class Solution {
	public static String findLCS(String X, String Y) {
		// Write your code here...
		int n = X.length(), m = Y.length();
		int[][] dp = new int[n + 1][m + 1];
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (X.charAt(i - 1) == Y.charAt(j - 1)) {
					dp[i][j] = dp[i - 1][j - 1] + 1;
				} else {
					dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		int i = n, j = m;
		while (i > 0 && j > 0) {
			if (X.charAt(i - 1) == Y.charAt(j - 1)) {
				sb.append(X.charAt(i - 1));
				i--;
				j--;
			} else if (dp[i - 1][j] > dp[i][j - 1]) {
				i--;
			} else {
				j--;
			}
		}
		return sb.reverse().toString();
	}
}

```
