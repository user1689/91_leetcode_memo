## 题目
https://leetcode-cn.com/problems/word-ladder/

## 思路
BFS

## python3
```python3
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # s = set()
        dic = dict()
        for word in wordList:
            dic[word] = 1
        queue = deque()
        queue.append(beginWord)
        step = 1
        while (queue):
            size = len(queue)
            for _ in range(size):
                word = queue.popleft()
                if (word == endWord):
                    return step
                for i in range(len(word)):
                    tmp = word
                    for j in range(26):
                        tmp = tmp[:i] + chr(j + ord('a'))+ tmp[i+1:]              
                        if (tmp in dic and dic[tmp] == 1):
                            queue.append(tmp)
                            dic[tmp] -= 1
            step += 1
        return 0
```

## 复杂度分析
* time O(n * c * 26) c is the length of words
* space O(n)

## 相关题目
1. https://leetcode-cn.com/problems/word-ladder-ii/
