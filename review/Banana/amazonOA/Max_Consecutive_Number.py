from typing import List

class solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        ll, rr = 0, 0
        cnt, res = 0, 0
        n = len(arr)
        while (rr < n):
            # add arr[rr] for judgement 
            if (arr[rr] == 0):
                cnt+=1

            # move ll until subarray is valid
            while (ll <= rr and cnt > k):
                if (arr[ll] == 0):
                    cnt-=1
                ll+=1
            
            # calculate answer
            res = max(res, rr - ll + 1)
            
            rr+=1
        return res
    
obj = solution()
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
k = 2
res = obj.longestOnes(arr, 2)
print(res)

