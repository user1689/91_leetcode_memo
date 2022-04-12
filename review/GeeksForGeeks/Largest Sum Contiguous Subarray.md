## 题目
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

## python3
```python3
#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        dp = [0] * N
        dp[0] = arr[0]
        for i in range(1, N):
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
        res = max(dp)
        return res
```
