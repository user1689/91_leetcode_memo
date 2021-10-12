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
        # 思路一
        # bruteForce TLE!!!
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
        
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # time nlogn 堆排序
        # space n indices数组空间大小
        # 思路二
        # sort + minHeap
        n = len(tasks)
        indices = list(range(n))
        # 将task按照开始时间进行排序
        indices.sort(key = lambda x: tasks[x][0])
        
        ans = list()
        heap = list()
        timeStamp = 0
        # 用于指向indices 
        # 因为indices已经按照tasks[x][0]排序过，所以ptr直接在indices中按顺序往后移动判断开始时间是和否存小于等于timeStamp
        ptr = 0
        for i in range(n):
            # 加速 如果没有可以执行的任务，直接快进
            if not heap:
                timeStamp = max(timeStamp, tasks[indices[ptr]][0])
            # 将所有开始时间小于timeStamp的都加入队列
            while ptr < n and (tasks[indices[ptr]][0] <= timeStamp):
                heapq.heappush(heap, (tasks[indices[ptr]][1], indices[ptr]))
                ptr += 1
            # 选择处理时间最小的任务
            process, idx = heapq.heappop(heap)
            timeStamp = timeStamp + process
            ans.append(idx)
        return ans
```

## 复杂度分析 
* time nlogn
* space n

## 相关题目
1. 待补充
