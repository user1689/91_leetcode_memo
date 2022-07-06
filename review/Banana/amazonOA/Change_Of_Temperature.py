from typing import List


class solution:
    def changeOfTemperature(self, arr:List[int]):
        n = len(arr)
        preSum = [0 for _ in range(n + 1)]
        for i in range(0, n):
            preSum[i+1] = preSum[i] + arr[i]
        res = -0x3f3f3f
        for i in range(1, n+1):
            tmp1 = preSum[i] - preSum[0]
            tmp2 = preSum[n] - preSum[i-1]
            res = max(tmp1, max(res, tmp2))
        return res   
      	
obj = solution()
arr = [6,-2,5]
res = obj.changeOfTemperature(arr)
print(res)