## 题目
https://leetcode-cn.com/problems/number-of-boomerangs/submissions/

## 思路
哈希表+排列数

## python3
```python
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        
        # time n**2
        # space 1
        # 思路一
        # 枚举 + 哈希表

        ans = 0
        for p in points:
            dic = defaultdict(int)
            for q in points:
                dis = (q[0] - p[0]) * (q[0] - p[0]) + (q[1] - p[1]) * (q[1] - p[1])
                # {char:frequency}
                dic[dis] += 1
            for value in dic.values():
                # 大于1就求排列数并累加答案
                if value > 1:
                    # 排列:第一个空位有n个可以选，第二个空位有(n - 1)个可以选
                    # 即n * (n - 1)
                    ans += value * (value - 1)
            # print(dic)
        return ans
```

## 复杂度分析
* time n**2 
* space n

## 相关题目
1. https://leetcode-cn.com/problems/line-reflection/
