## 题目
https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/solution/30-chuan-lian-suo-you-dan-ci-de-zi-chuan-bvy9/

## 思路
滑动窗口+哈希表

## python3
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # time n*m
        # space n
        # 思路一
        # 双哈希表
        # 第一个哈希表用于存储words中单词出现的频次
        # 第二个哈希表用于存储遍历过程中单词出现的频次

        allWords = collections.Counter(words)
        lengthWord = len(words[0])
        numOfWords = len(words)
        n = len(s)
        res = []
        for i in range(0, n - lengthWord * numOfWords + 1):
            subWords = collections.defaultdict(int)
            idx = i
            # 开始检查子串内部是否满足条件
            while idx < i + lengthWord * numOfWords:
                curWord = s[idx: idx+lengthWord]
                # 如果不存在或者存在的次数已经满了
                if curWord not in allWords or subWords[curWord] == allWords[curWord]:
                    break
                subWords[curWord] += 1
                idx = idx + lengthWord
            # 此时如果idx位于末尾表示满足条件 即没有被break过
            if idx == i + lengthWord * numOfWords:
                res.append(i)
        return res
```

## 复杂度分析
* time n*m n为s长度 m为lengthWord * numOfWords
* space n

## 相关题目
1. 待补充
