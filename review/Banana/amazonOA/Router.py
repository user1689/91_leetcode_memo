from typing import List
class solution:
    def router(self, buildingCount: List[int], routerLocation: List[int], routerRange: List[int]) -> int:
        
        n = len(buildingCount)
        cnt = [0] * (n + 2)
        for i in range(0, len(routerLocation)):
            cnt[max(1, routerLocation[i] - routerRange[i])] += 1
            cnt[min(n+1, routerLocation[i] + routerRange[i] + 1)] -= 1
        # [0,1,0,0,0,-1,0] n+1 -> 0 ~ n -> 1 ~ n+1
        # print(cnt)
        ans = 0
        preSum = 0
        for i in range(1, n+1):
            preSum += cnt[i]
            if (preSum >= buildingCount[i - 1]):
                ans += 1 
        return ans


obj = solution()
a = [1,4,2,3,2]
  # [0,1,1,3,4,2]
# [0,0,1,0,2,1,-2] -> [0,0,1,1,3,4,2]
b = [3,5,5]
c = [1,1,1]
res = obj.router(a, b, c) 
print(res)