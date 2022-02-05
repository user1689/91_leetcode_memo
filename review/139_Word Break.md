## 题目
https://leetcode-cn.com/problems/word-break/

## 思路
DFS, BFS, DP

## python3
```python3
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache
        def dfs(s, startIdx):
            if (startIdx == len(s)):
                return True
            
            for end in range(startIdx, len(s)):
                if (s[startIdx:end+1] in hashSet):
                    if dfs(s, end+1):
                        return True
                
            return False

        hashSet = set()
        for word in wordDict:
            hashSet.add(word)
        return dfs(s, 0)
'''
        apple
        /
    pen
    /
apple
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:   

        visited = [0] * len(s)
        queue = collections.deque()
        queue.append(0)
        while (queue):
            size = len(queue)
            for _ in range(size):
                startIdx = queue.popleft()
                # 访问过了如果没有返回true说明就不可能有答案
                if (visited[startIdx]):
                    continue
                else:
                    visited[startIdx] = 1
                for end in range(startIdx, len(s)):
                    if s[startIdx:end+1] in wordDict:
                        # 包头不包尾所以
                        # 到达len(s)-1表示已经全部切割完成
                        if (end == len(s) - 1):
                            return True
                        else:
                            queue.append(end+1)
        return False
```

## 复杂度分析
* time ?
* space n

## 相关题目
1. 待补充
