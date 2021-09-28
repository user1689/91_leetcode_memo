## 题目
https://leetcode-cn.com/problems/two-sum/submissions/

## 思路
暴力，哈希表优化

## python
```python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # time n
        # space n
        # 思路二
        # hashTable

        dic = dict()
        for idx, num in enumerate(nums):
            if (target - num) in dic:
                return [dic[(target - num)], idx]
            dic[num] = idx

```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/3sum/
2. https://leetcode-cn.com/problems/4sum/
