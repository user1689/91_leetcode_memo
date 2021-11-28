## 题目
https://leetcode-cn.com/problems/combination-sum/

## 思路
DFS

## python3
```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # time n * 2**n
        # space target
        # 二进制枚举
        def dfs(idx, path, total):
            if total > target:
                return
            # 顺序有差别的 这么写当idx==len（candidates）时也可以加入
            if total == target:
                res.append(path[:])
                return

            if idx == len(candidates):
                return 

            # 不选
            dfs(idx + 1, path, total)

            # 选
            if candidates[idx] <= target - total:
                path.append(candidates[idx])
                dfs(idx, path, total + candidates[idx])
                path.pop()
                
        res = []
        path = []
        dfs(0, path, 0)
        
        return res
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # time (n+m-1)! / m!(n-1)!
        # space target
        def dfs(startIdx, path, total):
            if total > target:
                return
            
            if total == target:
                res.append(path)
                return
            
            for i in range(startIdx, len(candidates)):
                dfs(i, path + [candidates[i]], total + candidates[i])
                
        res = []
        path = []
        dfs(0, path, 0)
        
        return res
```

## 时间复杂度
* time n * 2**n
* space target

## 相关题目
1. https://leetcode-cn.com/problems/combination-sum-ii/
2. https://leetcode-cn.com/problems/combination-sum-iii/
3. https://leetcode-cn.com/problems/combination-sum-iv/
