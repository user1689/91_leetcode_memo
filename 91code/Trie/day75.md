## 题目
https://leetcode-cn.com/problems/multi-search-lcci/

## 思路
Trie

## python3
```python3
class Trie:
    def __init__(self):
        self.trie = {}
 
    def insert(self, word):
        cur = self.trie
        for w in word:
            if w not in cur:
                cur[w] = {}
                cur = cur[w]
            else:
                cur = cur[w]
        cur['#'] = word
    
    def search(self, word):
        res = []
        cur = self.trie
        for w in word:
            if w not in cur:
                break
            cur = cur[w]
            if '#' in cur:
                res.append(cur['#'])
        return res

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        t = Trie()
        for word in smalls:
            t.insert(word)
        
        hint = defaultdict(list)
        for i in range(0, len(big)):
            tmp = t.search(big[i:])
            for word in tmp:
                hint[word].append(i)

        res = []
        for ss in smalls:
            res.append(hint[ss])
        return res
```

## 复杂度分析
* time n*m n=len(big)，m=len(smalls)
* space m*max(len(smalls[i]))

## 相关题目
1. 待补充
