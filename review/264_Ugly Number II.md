## 题目
https://leetcode-cn.com/problems/ugly-number-ii/

## 思路
多路归并

## python3
```python3
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # time n**2
        # space n
        primeFactors = [2, 3, 5]
        heap = [1]
        s = set()
        s.add(1)
        i = 1
        while(i <= n):
            x = heapq.heappop(heap)
            if (i == n):
                return x
            for prime in primeFactors:
                y = x * prime
                if y not in s:
                    s.add(y)
                    heapq.heappush(heap, y)
            i += 1
        return -1

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 多路归并
        # time n 
        # space n
        tmp = [0] * (n + 1)
        tmp[1] = 1
        ptr2, ptr3, ptr5 = 1, 1, 1
        k = 2
        res = []
        while(k <= n):
            a = tmp[ptr2] * 2
            b = tmp[ptr3] * 3
            c = tmp[ptr5] * 5  
            minVal = min(min(a, b), c)
            if (a == minVal):
                ptr2 += 1
            if (b == minVal):
                ptr3 += 1
            if (c == minVal):
                ptr5 += 1
            tmp[k] = minVal
            k += 1
        return tmp[n]
```

## 复杂度分析
* time n
* space n

## 相关题目
1. https://leetcode-cn.com/problems/super-ugly-number/
