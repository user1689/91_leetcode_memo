## 题目
https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies/

## 思路
拓扑排序

## python3
```python3
class Solution:
    def tp_sort(self, items, indegree, neighbors): 
        q = collections.deque([])
        ans = []
        for item in items:
            if not indegree[item]:
                q.append(item)
        while q:
            cur = q.popleft()
            ans.append(cur)

            for neighbor in neighbors[cur]:
                indegree[neighbor] -= 1
                if not indegree[neighbor]:
                    q.append(neighbor)
        return ans

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        max_group_id = m
        for project in range(n):
            if group[project] == -1:
                group[project] = max_group_id
                max_group_id += 1
        
        project_indegree = collections.defaultdict(int)
        group_indegree = collections.defaultdict(int)
        project_neighbors = collections.defaultdict(list)
        group_neighbors = collections.defaultdict(list)
        group_projects = collections.defaultdict(list)

        for project in range(n):
            group_projects[group[project]].append(project)
        
            for pre in beforeItems[project]:
                if group[pre] != group[project]:
                    group_indegree[group[project]] += 1
                    group_neighbors[group[pre]].append(group[project])
                else:
                    project_indegree[project] += 1
                    project_neighbors[pre].append(project)
        
        ans = []
        group_queue = self.tp_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)

        if len(group_queue) != max_group_id:
            return []

        for group_id in group_queue:

            project_queue = self.tp_sort(group_projects[group_id], project_indegree, project_neighbors)

            if len(project_queue) != len(group_projects[group_id]):
                return []
            
            ans += project_queue

        return ans
```

## 时间复杂度
* time n + m  n 为点数，mm 为边数
* space n + m  n 为点数，mm 为边数

## 相关题目
1. https://leetcode-cn.com/problems/course-schedule/
2. https://leetcode-cn.com/problems/course-schedule-ii/
