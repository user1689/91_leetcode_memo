from typing import List;
class solution:
    def pascalTriangle(self, arr: List[int]) -> str:
        n = len(arr)
        for i in range(0, n - 2):
            for j in range(0, n - i - 1):
                x = arr[j]
                y = arr[j+1]
                t = (x + y) % 10
                arr[j] = t
        return str(arr[0]) + str(arr[1])

obj = solution()
arr = [4,5,6,7,9]
res = obj.pascalTriangle(arr)
print(res)

