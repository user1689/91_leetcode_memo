from typing import List


class Solution:
    def mergeInterval(self, interval:List[List[int]]) -> int:
        interval.sort(key=lambda x: x[1], reverse=False)
        i = 0 
        cnt = 0
        n = len(interval)
        while (i < n):
            j = i+1
            while (j < n and interval[j][0] <= interval[i][1]):
                j+=1
                cnt+=1
            i = j
        return cnt

obj = Solution()
arr = [[1,3],[0,1],[3,4]]
res = obj.mergeInterval(arr)
print(res)