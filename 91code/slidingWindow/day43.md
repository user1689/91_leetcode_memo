## 题目
https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

## 思路
imitation

## python3
```python3
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # time n
        # space n
        Vowels = {'a','e','i','o','u'}
        # queue = collections.deque()

        # 初始化窗口
        i = 0
        cnt = 0
        for j in range(k):
            if s[j] in Vowels:
                cnt += 1

        # 菜鸡滑动窗口
        n = len(s)
        maxCnt = cnt
        while j < n - 1:
            if s[i] in Vowels:
                cnt -= 1
            if s[j+1] in Vowels:
                cnt += 1
            i += 1
            j += 1  
            maxCnt = max(maxCnt, cnt)
        return maxCnt
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/sliding-window-maximum/
