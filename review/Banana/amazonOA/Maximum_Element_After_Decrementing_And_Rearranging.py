from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        '''
        [2,2,1,2,1]
         i j

        +- null/1 0/000 min/max odd/even repeated order/permutation
        '''
        arr.sort()
        if (arr[0] != 1):
            arr[0] = 1
        for i in range(0, len(arr) - 1):
            if (arr[i + 1] > arr[i] + 1):
                arr[i + 1] = arr[i] + 1
        return max(arr)

obj = Solution()
arr = [2,2,1,2,1]
res = obj.maximumElementAfterDecrementingAndRearranging(arr)
print(res)

