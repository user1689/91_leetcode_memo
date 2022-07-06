from typing import List

class solution:
    def miniMoves(self, arr: List[int]) -> int:
        n = len(arr)
        cntZero = 0
        cntOne = 0
        ans1 = 0
        for i in range(0, n):
            if (arr[i] == 1):
                cntOne+=1
            else:
                ans1+=cntOne

        ans2 = 0
        for j in range(0, n):
            if (arr[j] == 0):
                cntZero+=1
            else:
                ans2+=cntZero

                
        ans = ans1 if ans1 < ans2 else ans2
        return ans

obj = solution()
res = obj.miniMoves([1, 1, 1, 1, 0, 1, 0, 1])
print(res)
 