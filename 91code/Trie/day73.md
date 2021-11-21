## 题目
https://leetcode-cn.com/problems/implement-trie-prefix-tree/

## 思路
dict, TreeNode

## python3
```python3
class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        cur = self.trie
        for w in word:
            if w not in cur:
                cur[w] = {} 
                cur = cur[w]
            else:
                cur = cur[w]
        cur['#'] = {}

    def search(self, word: str) -> bool:
        cur = self.trie
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        if '#' in cur:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for pre in prefix:
            if pre not in cur:
                return False
            cur = cur[pre]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

## 复杂度分析
* time |s|
* space sigma|s|

## 相关题目
1. https://leetcode-cn.com/problems/implement-magic-dictionary/
2. https://leetcode-cn.com/problems/replace-words/
3. https://leetcode-cn.com/problems/design-add-and-search-words-data-structure/
