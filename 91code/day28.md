## 题目
https://leetcode-cn.com/problems/sliding-window-maximum/

## 思路
bruteForce, minStack

## python
```python3
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # 思路
        # 利用双端队列记录当前滑动窗口的元素索引
        # 队列最左侧元素记录滑动窗口中最大元素的索引
        # 遍历数组：
        #   如果队列最左侧索引已不在滑动窗口范围内，弹出队列最左侧索引
        #   通过循环确保队列的最左侧索引所对应元素值最大
        #   新元素入队
        #   从第一个滑动窗口的末尾索引开始将最大值存储到结果res中

        res = []
        deque = collections.deque()
        for idx, num in enumerate(nums):
            # 当最大元素脱离窗口时 表明此时它已经不是最大元素了
            if deque and deque[0] == (idx - k):
                deque.popleft()
            # 更新此时的最大元素 维护一个单调递减栈
            while deque and nums[deque[-1]] < num:
                deque.pop()
            deque.append(idx)
            # 此时表明窗口已经初始化完成 需要开始计算最大值了
            if idx >= k - 1:
                res.append(nums[deque[0]])
        return res
```

## 时间复杂度
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/minimum-window-substring/
