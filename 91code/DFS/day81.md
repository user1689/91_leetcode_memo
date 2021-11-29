## 题目
https://leetcode-cn.com/problems/combination-sum-ii/

## 思路
DFS(backTracking)

## python3
```python3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(startIdx, total, path):
            if total == target:
                res.append(path)
                return
            if startIdx == n:
                return
            
            for i in range(startIdx, n):
                if i > startIdx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    continue
                dfs(i+1, total + candidates[i], path+[candidates[i]])
            
        res = []
        path = []
        candidates.sort()
        n = len(candidates)
        dfs(0, 0, path)
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # time (2**n) * m (n为candidates长度, m 为 freq长度)
        # space n
        # 二进制枚举 + freq(hashTable)

        def dfs(idx, rest, sequence):
            # nonlocal sequence
            if (rest == 0):
                ans.append(sequence)
                return

            if (idx == len(freq)) or (freq[idx][0] > rest):
                return
            
            # 开始决定选还是不选

            # 不选当前数
            dfs(idx+1, rest, sequence)

            # 选当前数
            # 计算最多可以选几个
            most = min(rest // freq[idx][0], freq[idx][1])
            for i in range(1, most+1):
                # sequence.append(freq[idx][0])
                dfs(idx+1, rest - (i * freq[idx][0]), sequence + (i * [freq[idx][0]]))
            # sequence = sequence[:-most]

        tmp = collections.Counter(candidates)
        freq = sorted(tmp.items())
        ans = list()
        sequence = list()
        dfs(0, target, sequence)
        return ans
```

## 复杂度分析
* time n*2**n
* space n

## 相关题目
1. 待补充
