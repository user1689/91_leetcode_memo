from typing import List

class solution:
    def findMaxInKSizeSubarrayWithNoRepeated(self, arr:List[int], k: int):
        '''
        [1,2,7,7,4,3,6], k = 3
        i   j
        '''
        n = len(arr)
        preSum = [0] * (n + 1)
        for i in range(0, len(arr)):
            preSum[i+1] = preSum[i] + arr[i] 
        i, j = 0, 0
        
        res = 0
        seen = set()
        tmp = []
        while (j < n):
            while (i < n and j - i + 1> k):
                seen.remove(arr[i])
                i+=1

            while (i < n and arr[j] in seen):
                seen.remove(arr[i])
                i+=1
            
            if (j - i + 1 == k):
                tmp.append([i, j])

            seen.add(arr[j])
            j+=1
        
        for l, r in tmp:
            print(l)
            print(r)
            res = max(res, preSum[r+1] - preSum[l])
        return res
                

obj = solution()
arr = [1,2,7,7,4,3,9,3]
k = 3
res = obj.findMaxInKSizeSubarrayWithNoRepeated(arr, k)
print(res)