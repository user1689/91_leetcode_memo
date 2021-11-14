## 题目
https://leetcode-cn.com/problems/assign-cookies/

## 思路
Greedy

## python3
```python3
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0 
        j = 0
        count = 0
        while(i < len(g) and j < len(s)):
            # 如果此时孩子的食量比饼干分量大,那么在不超出范围的情况下，往后遍历
            while(j < len(s) and s[j] < g[i]):
                j += 1
            # 如果在有限饼干范围内，找到了满足孩子胃口的那一块，就继续往后遍历，并且计数值+1
            if (j < len(s)):
                count += 1
            i += 1
            j += 1
        return count
            

```

## 复杂度分析
* time nlogn + mlogm
* space 1

## 相关题目
1. 待补充
