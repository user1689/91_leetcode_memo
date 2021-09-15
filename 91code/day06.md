## 题目
https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii/submissions/

## 思路
* 计数
* 计数优化
* 单调栈

## python3
```python3
# 思路一
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        # time n**2 
        # space n
        # 思路二
        # 哈希表
        # 计数
        # 这两个数组排序后的结果以及计数信息是一致的

        c1 = defaultdict(int)
        c2 = defaultdict(int)
        ans = 0
        for a, b in zip(arr, sorted(arr)):
            c1[a] += 1
            c2[b] += 1
            if c1 == c2: ans += 1
        return ans
        
# 思路二
# 优化复杂度
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        # time nlogn 
        # space n
        # 思路二
        # 哈希表
        # 计数
        # 这两个数组排序后的结果以及计数信息是一致的
        # 优化空间复杂度和时间复杂度
        # 用变量 nonzero 来计数目前差值不等于 0 的字符的个数

        c = defaultdict(int)
        ans = 0
        nonzero = 0
        for a, b in zip(arr, sorted(arr)):
            c[a] += 1
            if c[a] == 1: nonzero += 1
            if c[a] == 0: nonzero -= 1
            
            c[b] -= 1
            if c[b] == -1: nonzero += 1
            if c[b] == 0: nonzero -= 1
            
            if nonzero == 0: ans += 1
        return ans
        
# 思路三
# 单调栈
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        # time n
        # space n
        # 思路一
        # 单调递增栈
        # 假设head为每个块中最大元素 
        # 我们在在栈中只存head
        # 需要注意的是如果新元素小于前面几个head那么都需要一起融合了

        stack = []
        for num in arr:
            # 当num < stack[-1] 说明需要融合
            if stack and stack[-1] > num:
                # 融合之前 先存下 head
                head = stack.pop()
                # 此步骤看是否需要融合前面其他的head
                while stack and stack[-1] > num:
                    stack.pop()
                stack.append(head)
            else:
                # num > stack[-1]时直接加入作为新head, 不需要融合
                stack.append(num)
        return len(stack)
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/max-chunks-to-make-sorted/
