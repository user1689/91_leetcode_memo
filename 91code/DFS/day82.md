## 题目
https://leetcode-cn.com/problems/permutations-ii/

## 思路
DFS

## python3
```python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # time n * n!
        # space n
        # permutationUnique
        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
            
            for i in range(0, len(nums)):
                if visited[i]:
                    continue
                '''
                我是这样理解的，for循环保证了从数组中从前往后一个一个取值，再用if判断条件。所以nums[i - 1]一定比
                nums[i]先被取值和判断。如果nums[i - 1]被取值了，那vis[i - 1]会被置1，只有当递归再回退到这一层时
                再将它置0。每递归一层都是在寻找数组对应于递归深度位置的值，每一层里用for循环来寻找。所以当vis[i - 1] == 1时，说
                明nums[i - 1]和nums[i]分别属于两层递归中，也就是我们要用这两个数分别放在数组的两个位置，这时不需
                要去重。但是当vis[i - 1] == 0时，说明nums[i - 1]和nums[i]属于同一层递归中（只是for循环进入下一
                层循环），也就是我们要用这两个数放在数组中的同一个位置上，这就是我们要去重的情况。
                '''
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                dfs(path + [nums[i]])
                visited[i] = False

        # 保证所有一样的数字在一起，这样才能够进行剪枝
        nums.sort()
        visited = [False] * len(nums)
        res = []
        path = []  
        dfs(path)
        return res
```

## 复杂度分析
* time n * n!
* space n

## 相关题目
1. 待补充
