## 题目
https://leetcode-cn.com/problems/find-the-town-judge/

## 思路
有向图

## python3
```python3
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # time n
        # space n
        # 有向图
        indegree = [-1] + [0 for _ in range(n)]
        outdegree = [-1] + [ 0 for _ in range(n)]

        for element in trust:
            peopleTrustOthersIdx = element[0]
            trustPeopleIdx = element[1]

            indegree[trustPeopleIdx] += 1
            outdegree[peopleTrustOthersIdx] += 1

        for idx, element in enumerate(indegree):
            if element == (n - 1):
                if outdegree[idx] == 0:
                    return idx
        return -1
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/find-the-celebrity/
