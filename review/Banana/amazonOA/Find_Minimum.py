'''
    [7, 3, 6, 1]
  [0,7,10,16,17]
   l    r
'''
from typing import List


class solution:
    def maxDelete(self, k:int, arr:List[int]):
        n = len(arr)
        preSum = [0] * (n + 1)

        total = 0
        for i in range(0, n):
            total += arr[i]
            preSum[i+1] = preSum[i] + arr[i]
        
        res = float('inf')
        l, r = 0, k
        while (r < n):
            curSum = preSum[r] - preSum[l]
            res = min(total - curSum, res)
            l+=1
            r+=1
        return res
        
obj = solution()
res = obj.maxDelete(2, [7,3,6,1])
print(res)