from typing import List

class solution:
    def NDSWAMKN(self, arr:List[int], k:int) -> int:
        seen = set()
        cnt = 0
        for i in range(0, len(arr)):
            tmp = []
            countOdds = 0
            for j in range(i, len(arr)):
                if (arr[j] & 1):
                    countOdds+=1
                if (countOdds <= k):
                    tmp.append(arr[j])
                    tmpKey = tuple(tmp)
                    if (tmpKey not in seen):
                        seen.add(tmpKey)
                        cnt+=1
        return cnt

obj = solution()
arr = [3,2,3]
res = obj.NDSWAMKN(arr, 1)
print(res)