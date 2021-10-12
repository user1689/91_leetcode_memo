## 题目
https://leetcode-cn.com/problems/single-threaded-cpu/

## 思路
小根堆, 排序+小根堆

## python3
```python3
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
     
        # time n * nlogn
        # space logn
        # simulation
        heap = []
        totalTime = 1
        for i in range(0, len(tasks)): # n
            totalTime += tasks[i][1]

        res = []
        time = 1
        taskEndTime = -1
        while time <= totalTime: # n
            for i in range(0, len(tasks)): # n
                if time == tasks[i][0]:  # 1
                    heapq.heappush(heap, (tasks[i][1], i))  # logn
            # 当前time大于等于endtime说明线程闲置 如果heap里有东西弹出执行
            if time >= taskEndTime and heap:
                taskDuration, taskIdx = heapq.heappop(heap)
                taskEndTime = time + taskDuration
                res.append(taskIdx)
            time += 1
        return res
        
```

## 复杂度分析
* time 
* space

## 相关题目
1. 待补充
