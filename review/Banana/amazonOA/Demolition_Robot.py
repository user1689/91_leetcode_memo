from collections import deque
from typing import List

class solution:
    def demolitionRobot(self, arr: List[List[int]]) -> int:
        
        row = len(arr)
        col = len(arr[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        visited[0][0] = 1
        q = deque()
        q.append((0,0))
        step = 0
        while (q):
            size =len(q)
            for _ in range(size):
                x, y = q.popleft()
                if (arr[x][y] == 9): return step
                for new_x, new_y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if (0<=new_x<row and 0<=new_y<col and not visited[new_x][new_y] and arr[new_x][new_y] != 0):
                        # if (arr[new_x][new_y] == 9): return step + 1
                        visited[new_x][new_y] = 1
                        q.append((new_x, new_y))
            step+=1
        return -1

obj = solution()
arr = [

    [1,1,1],
    [1,1,0],
    [1,1,9]

]
res = obj.demolitionRobot(arr)
print(res)


