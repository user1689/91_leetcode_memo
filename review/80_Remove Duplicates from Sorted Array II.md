## 题目
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

## python3
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        slow负责赋值 fast一直往后探 
        '''
        slow = 0
        for fast in range(0, len(nums)):
            if (slow < 2 or nums[slow - 2] != nums[fast]):
                nums[slow] = nums[fast]
                slow += 1
        return slow

#  0 0
#  0 0 0 
#  0 0 0 0 1 1 1
#  0 0 1 1
```
## 相关题目
1. https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
2. https://leetcode-cn.com/problems/remove-element/
