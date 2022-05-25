## 题目
https://leetcode.cn/problems/random-pick-index/

## 思路
[reserviour sampling](https://leetcode.cn/problems/random-pick-index/)

## python3
```python3
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.map = defaultdict(list)
        for i in range(0, len(self.nums)):
            self.map[self.nums[i]].append(i)

    def pick(self, target: int) -> int:
        return choice(self.map[target])  


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        ans = 0
        cnt = 0
        for i, num in enumerate(self.nums):
            if (num == target):
                cnt += 1
                if (randrange(0, cnt) == 0):
                    ans = i
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

## 复杂度分析
time O(N)
space O(1)

## 相关题目
1. 待补充
