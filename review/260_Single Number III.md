## 题目
https://leetcode-cn.com/problems/single-number-iii/

## 思路
bitManipulation

## python3
```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # time n
        # space 1
        # bitManipulation
        # 所有出现两次的相同元素，相互异或为0，那么全部异或得到最终答案的两个数的异或结果
        # 这个异或结果可以告诉我们他们俩哪些位是不同的
        ans = 0
        for num in nums:
            ans ^= num
        # 获取lowbit
        ans &= -ans

        # 分组进行划分
        ans1 = ans2 = 0
        for num in nums: 
            # 根据这位1将所有num分成两组，两个不同的数会在两组，其他仍然是相同的
            if num & ans == 0:
                ans1 ^= num
            # 如果这么划分是不对的
            # 因为 假设ans=2 num=2 2&2 = 2并不会等于1
            # 但是 假设ans=2 num=1 2&1 = 0是固定的
            # 再举一个例子 
            #     假设ans=2 num=3 2&3 = 0
            # elif num & ans == 1:
            else:
                ans2 ^= num
        return [ans1, ans2]
        
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        low bits 
        '''
        tmp = 0
        for num in nums:
            tmp ^= num
        groupDivider = tmp & (-tmp)
        ans1 = ans2 = 0
        for num in nums:
            if (num & groupDivider):
                ans1 ^= num
            else:
                ans2 ^= num
        return [ans1, ans2]
        
# reference https://leetcode-cn.com/problems/single-number-iii/solution/gong-shui-san-xie-yi-ti-shuang-jie-ha-xi-zgi4/
```

## 复杂度分析
* time n
* space 1

## 相关题目
1. 待补充
