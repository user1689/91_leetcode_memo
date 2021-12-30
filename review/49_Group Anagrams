## 题目
https://leetcode-cn.com/problems/group-anagrams/

## 思路
HashTable

## python3
```python3
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time n * (k + |sigma|)
        # space n * (k + |sigma|)
        # 思路一
        # 哈希表 {tmp:s} tmp为标记过后的数组
        dic = collections.defaultdict(list)

        # 一共有s个单词
        for s in strs:
            tmp = [0] * 26
            # k 每个单词长度为k
            for char in s:
                tmp[ord(char) - ord('a')] += 1
            # list需要转成tuple才hashable
            # |sigma| sigma为tmp长度
            dic[tuple(tmp)].append(s)

        res = []
        for value in dic.values():
            res.append(value)
        return res
```

## 复杂度分析
* time n * (k + |sigma|)  k is the length of each str in strs, sigma is the length of tmp 
* space n * (k + |sigma|)

## 相关题目
1. https://leetcode-cn.com/problems/valid-anagram/
