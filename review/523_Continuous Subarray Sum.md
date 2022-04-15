## 题目
https://leetcode-cn.com/problems/continuous-subarray-sum/

## 思路
preSum + hashTable + mod

## python3
```python3
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:


        '''
        10^5 -> nlogn

          [23, 2, 4, 6,7]
        [0,23,25,29,35,41]
        
        (29-23) % k = 0  
        -> (29%k) - (23%k) = 0
        -> (29%k) = (23%k)

        [0,0]
        1
        [0,0,0]
        
        '''

        preSum = [0] * (len(nums) + 1)
        dic = dict()
        dic[0] = 0
        for i in range(0, len(nums)):
            preSum[i + 1] = nums[i] + preSum[i]
        
        for i in range(1, len(preSum)):
            tmp = preSum[i]
            tmp %= k
            if (tmp in dic):
                if (i - dic[tmp] >= 2):
                    return True
            else:
                dic[tmp] = i
        return False
```

## 复杂度分析
* time O(N)
* space O(N)

## 相关题目
1. 待补充
