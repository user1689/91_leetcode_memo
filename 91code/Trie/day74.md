## 题目
https://leetcode-cn.com/problems/map-sum-pairs/

## 思路
Trie+DFS

## python3
```python3
class MapSum:

    def __init__(self):
        self.trie = {}
        self.val = 0

    def insert(self, key: str, val: int) -> None:
        cur = self.trie
        for k in key:
            if k not in cur:
                cur[k] = {}
                cur = cur[k]
            else:
                cur = cur[k]
        cur['#'] = val

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for pre in prefix:
            if pre not in cur:
                return 0
            else:
                cur = cur[pre]
        return self.dfs(cur)

    def dfs(self, cur: dict) -> int:
        ans = 0
        for k in cur:
            if k == '#':
                ans += cur[k]
            else:
                ans += self.dfs(cur[k])
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
```

## 复杂度分析
* time |s|
* space sigma|s|

## 相关题目
1. 待补充
