## 题目
https://leetcode-cn.com/problems/subarray-sum-equals-k/

## 思路
preSum + hashTable

## python3
```python3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
          [1,2,3]
        [0,1,3,6]
        
        10^4 -> n*sqrtn
        +- null/1 min/max odd/even repeated order/permutation


        '''
        # method1
        preSum = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            preSum[i + 1] = preSum[i] + nums[i]
        print(preSum)

        cnt = 0
        dic = dict()
        # method2
        # dic[0] = 1
        for i in range(0, len(preSum)):
            # 如果不这么写 就需要初始化map中放入0:1来防止漏掉cnt 
            # 或者在做presum的时候就从1开始赋值 避免后面的计算出错
            # eg: [0,1,2,8], k = 3
            # method3
            # if (preSum[i] == k):
            #     cnt += 1
            if (preSum[i] - k) in dic:
                cnt += dic[preSum[i] - k] 
            dic[preSum[i]] = dic.get(preSum[i], 0) + 1
        return cnt
        
        
        '''
        
        [1,1,1], k = 2
        [1,2,3]
        
        
        [1,1,1,-1,-1,-1,1,1,1], k = 2
        [1,2,3, 2, 1, 0,1,2,3]
        
        
        pre = 3
        pre - tmp = k -> pre - k = tmp
        if (pre - k in map):
            cnt += map[pre - k]
        
        [1,3,6]
        
        '''
        map = dict()
        map[0] = 1
        pre = 0
        cnt = 0
        for num in nums:
            pre += num
            if (pre - k in map.keys()):
                cnt += map[pre - k]
            map[pre] = map.get(pre, 0) + 1
        return cnt
```

## 时间复杂度
* time n
* space n

## 相关题目
1. 待补充
