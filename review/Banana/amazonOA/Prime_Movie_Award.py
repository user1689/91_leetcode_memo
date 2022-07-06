from typing import List


class solution:
    def primeMovieAward(self, arr:List[int], k:int):
        arr.sort()
        i, j = 0, 0
        n = len(arr)
        cnt = 0

        while (j < n):
            while (j < n and abs(arr[j] - arr[i]) <= k):
                j+=1
            cnt+=1
            i=j
        return cnt


obj = solution()
arr = [1, 5, 4, 6, 8, 9, 2, 1, 1, 2]
k = 3
res = obj.primeMovieAward(arr, k)
print(res)

