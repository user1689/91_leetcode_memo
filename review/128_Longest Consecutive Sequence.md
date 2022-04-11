## 题目
https://leetcode-cn.com/problems/longest-consecutive-sequence/

## python3
```python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''' 
        10^5 -> nlogn
        10^6-10^7 -> n
        +- null/1 0/000 min/max odd/even repeated order/permutation
        

        if (len(nums) == 0):
            return 0
        maxStep = 0
        ss = set(nums)
        for num in nums:
            step = 0
            while ((num - 1) in ss):
                num -= 1
                step += 1
            maxStep = max(maxStep, step)
        return maxStep + 1

        n^2的写法中重复遍历了每一条 比如第一条为x, x+1, x+2, x+3..x+k 第二次又从x+1, x+2, ... x+k再遍历了一次 (减法同理)
        为了避免重复遍历 只从头部出发 
        每次都找到可能的链头
        # 如何定义链头？ 如果x-1不存在与s中就说明是链头
        # 找到链头以后往后搜索看能爬多长
        # 维护一个最长maxLen
        '''

        max_step = 0
        ss = set(nums)
        for num in nums:
            if ((num - 1) not in ss):
                step = 0
                while (num in ss):
                    num += 1
                    step += 1
                max_step = max(step, max_step)
        return max_step
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/maximum-subarray/
2. https://leetcode-cn.com/problems/maximum-ascending-subarray-sum/
3. https://leetcode-cn.com/problems/continuous-subarray-sum/
4. https://leetcode-cn.com/problems/subarray-sum-equals-k/
5. https://leetcode-cn.com/problems/longest-increasing-subsequence/
6. https://www.geeksforgeeks.org/longest-sub-array-sum-k/
7. https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
