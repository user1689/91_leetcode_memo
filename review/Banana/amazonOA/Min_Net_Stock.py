from typing import List


class Solution:
    def minNetStock(self, arr:List[int]):
        n = len(arr)
        preSum = [0] * (n + 1)
        for i in range(0, n):
            preSum[i + 1] = arr[i] + preSum[i]
        tmp = 0x3f3f3f3f
        for i in range(0, n-1):
            fontPart = preSum[i+1] - preSum[0]
            postPart = preSum[n] - preSum[i+1]
            
            fontPart //= (i+1)
            postPart //= (n-(i+1))

            if (abs(fontPart - postPart) < tmp):
                tmp = abs(fontPart - postPart)
                res = i+1

        return res

obj = Solution()
arr = [1,3,2,3]
res = obj.minNetStock(arr)
print(res)