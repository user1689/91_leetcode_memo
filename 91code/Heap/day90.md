## 题目
https://leetcode-cn.com/problems/distant-barcodes/

## 思路
Sort, Heap

## python3
```python3
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # time n+nlogn
        # space n
        dic = dict()
        for num in barcodes:
            dic[num] = dic.get(num, 0) + 1
        
        tmp = sorted(dic.items(), key=lambda x: -x[1])
        res = []
        ans = [0] * len(barcodes)
        for key, freq in tmp:
            # tricky
            res += [key] * freq

        j = 0
        for i in range(0, len(res), 2):
            ans[i] = res[j]
            j += 1

        for i in range(1, len(res), 2):
            ans[i] = res[j]
            j += 1
        return ans
```
## 复杂复分析
* time n + nlogn
* space n

## 相关题目
1. 待补充
