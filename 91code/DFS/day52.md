## 题目
https://binarysearch.com/problems/Shortest-Cycle-Containing-Target-Node/submissions/2018136797

## 思路
BFS+set

## python3
```python3
class Solution:
    def solve(self, graph, target):
        # corner case:
        # graph = [
        #  [1],
        #  [1]
        # ]
        # target = 0
        queue = collections.deque([target])
        s = set()
        step = 0
        while (queue):
            size = len(queue)
            for _ in range(size):
                begin = queue.popleft()
                s.add(begin)
                for neighbor in graph[begin]:
                    if neighbor not in s:
                        queue.append(neighbor)
                    elif neighbor == target:
                        return step + 1
            step += 1
        return -1
```

## 复杂度分析
* time v + e  v 节点数, e 为边数
* space v

## 相关题目
1. 待补充
