## 题目
https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero/

## 思路
slidingWindow, Hash+Prefix

## python3
```python3
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 思路来自 @yanglr 
        # 题目要求删掉数组nums的左右两端的元素，并且删掉的元素和为target，也就是留下中间连续的子数组，其和为sum(nums) - target;
        # 题目还让求出最小的操作次数，即删掉的元素个数越少越好，也就是留下的中间子数组的长度越大越好。
        # 那么问题就转化为了找数组中间和为sum(nums) - target的最长子数组，令该表达式为我们的新目标new_target, 并将原数组的长度记作N。
        # https://github.com/yanglr

        # time n
        # space 1
        # slidingWindow/twoPointers
        total = sum(nums)
        count = total - x
        if count < 0:
            return -1
        if count == 0:
            return len(nums)
        
        left = 0
        curSum = 0
        maxLen = -1
        for right in range(0, len(nums)):
            curSum += nums[right]
            while left <= right and (curSum > count):
                curSum -= nums[left]
                left += 1
            if curSum == count and (right - left + 1 > maxLen):
                maxLen = max(maxLen, right - left + 1)
            right += 1
        return len(nums) - maxLen if maxLen != -1 else -1
        
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # time n
        # space n
        # preSum
        total = sum(nums)
        if total == x:
            return len(nums)
        target = total - x
        dic = collections.defaultdict(int)
        # 没有建立preSum数组但是需要做一个dummy所以先初始化下 preSum为0在idx-1位置
        dic[0] = -1
        preSum = 0
        maxLen = -1
        for i in range(0, len(nums)):
            preSum += nums[i]
            if (preSum - target in dic):
                left = dic[preSum - target] + 1
                right = i
                maxLen = max(maxLen, (right - left + 1)) 
            if preSum not in dic:
                dic[preSum] = i
        # print(maxLen)
        # print(dic)
        return len(nums) - maxLen if maxLen != -1 else -1
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
