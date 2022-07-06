
from typing import List
class solution:
    def maxPackage(self, packageWeights: List[int]) -> int:
        # stack = []
        # i = 0
        # n = len(packageWeights)
        # while (i < n):
        #     while (stack and stack[-1] < packageWeights[i]):
        #         packageWeights[i] += stack.pop()

        stack = []
        n = len(packageWeights)
        ans = 0
        stack.append(packageWeights[-1])
        for i in range(n - 2, -1, -1):
            if (packageWeights[i] < stack[-1]):
                stack.append(stack.pop() + packageWeights[i])
            else:
                stack.append(packageWeights[i])
            ans = max(ans, stack[-1])
        return ans

obj = solution()
arr = [2,9,10,3,7]
res = obj.maxPackage(arr)
print(res)