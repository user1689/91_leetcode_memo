## 题目
https://leetcode-cn.com/problems/super-ugly-number/

## 思路
多路归并

## python3
```python3
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 多路归并
        heap = []
        for i, num in enumerate(primes):
            heapq.heappush(heap, (num, i, 0))

        ans = [0] * n
        ans[0] = 1
        j = 1
        while(j < n):
            val, i, idx = heapq.heappop(heap)
            # 和前一个数字对比
            # 判断val是否有重复
            if (ans[j - 1] != val):
                # 如果没有重复就赋值完j自增1
                ans[j] = val
                j += 1
            # 算出下一个的答案
            # val * primes[i] == ans[idx + 1] * primes[i]
            heapq.heappush(heap, (ans[idx + 1] * primes[i], i, idx + 1))
        # print(ans)
        return ans[n - 1]
            
```

## 复杂度分析
* time max(nlogm, mlogm)
* space n

## 相关题目
1. 待补充
