## 题目
https://practice.geeksforgeeks.org/problems/longest-bitonic-subsequence0824/1/#

## 思路
longest increase subsequence

## python3
```python3
#User function Template for python3

class Solution:
    def find_longest_increase_subsequence(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(0, n):
            for j in range(0, i):
                if (nums[j] < nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
         
        return dp
        
	def LongestBitonicSequence(self, nums):
		# Code here
		'''
		   12
           20 7 9 6 9 21 12 3 12 16 1 27
           1  1 2 1 2 3  3  1  3  4 1 5
                                  
           6
		'''
		a = self.find_longest_increase_subsequence(nums)
		b = self.find_longest_increase_subsequence(nums[::-1])
		ans = 0
		tmp = b[::-1]
        for i in range(0, len(a)):
            ans = max(ans, a[i] + tmp[i])
        return ans - 1

```
