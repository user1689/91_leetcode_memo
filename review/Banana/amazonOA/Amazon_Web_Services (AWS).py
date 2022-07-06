from collections import deque
from typing import List

class solution:
    def awsCluster(self, bootingPower:List[int], processingPower:List[int], powerMax:int) -> int:
        
        n = len(bootingPower)
        i, j = 0, 0
        curProcessingPower = 0
        q = deque()
        res = 0
        while (j < n):

            while (q and bootingPower[q[0]] <= bootingPower[j]):
                q.popleft()
            q.append(j)    
      
            curProcessingPower += processingPower[j]
            powerNow = bootingPower[q[0]] + curProcessingPower * (j - i + 1)

            while (i <= j and powerNow > powerMax):
                curProcessingPower -= processingPower[i]
                if (i == q[0]): q.popleft()
                i+=1
            
            res = max(res, j - i + 1)

            j+=1

        return res
  

obj = solution()
bootingPower = [3, 6, 1, 3, 4]
processingPower = [2, 1, 3, 4, 5]
maxPower = 25
bootingPower2 = [9]
processingPower2 = [9]
maxPower2 = 17
res = obj.awsCluster(bootingPower2, processingPower2, maxPower2)
print(res) 

# https://leetcode.com/tag/two-pointers/discuss/1636493/Amazon-or-OA-or-Max-Length-of-Valid-Server-Cluster/1304119/