## 题目
https://leetcode-cn.com/problems/beautiful-array/

## 思路
divideAndConquer

## python3
```python3
class Solution:
    def beautifulArray(self, n: int) -> List[int]:

        def dfs(arr):
            if len(arr) <= 2:
                return arr
            a = dfs(arr[::2])
            b = dfs(arr[1::2])
            return a + b
        
        # 因为挨着的数比如1/2/3/4/5， 2*2=1+3， 3*2=2+4，因此把挨着的数打散即可
        lists = list(range(1,n+1))
        return dfs(lists)
```

## 复杂度分析
* time nlogn
* space nlogn

## 相关题目
1. 待补充
