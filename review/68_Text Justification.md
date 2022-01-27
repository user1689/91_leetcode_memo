## 题目
https://leetcode-cn.com/problems/text-justification/

## 思路
imitation

## python3
```python3
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def blank(n):
            return ' ' * n
        '''
        比较tricky的点是算多余的空格
        多余的空格可以用numSpaces % (wordNums - 1)来求出
        然后将前numSpaces % (wordNums - 1)个单词直接多补一个空格即可
        '''
        def rearrange(words, maxWidth):
            res = []
            right = 0
            n = len(words)
            while (True):
                left = right
                subLen = 0
                # 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
                while (right < n and subLen + len(words[right]) + right - left <= maxWidth):
                    subLen += len(words[right])
                    right += 1
                
                # 当为最后一行 单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
                if (right == n):
                    s = " ".join(words[left:])
                    res.append(s + blank(maxWidth - len(s)))
                    break

                wordNums = right - left
                wordSpaces = maxWidth - subLen
                # 当此行只有一个单词时 单词左对齐 
                if (wordNums == 1):
                    res.append(words[left] + blank(wordSpaces))
                    continue
                
                # 当前行不只一个单词
                avgSpaces = wordSpaces // (wordNums - 1)
                extraSpaces = wordSpaces % (wordNums - 1)
                s1 = blank(avgSpaces + 1).join(words[left : left + extraSpaces + 1])
                s2 = blank(avgSpaces).join(words[left + extraSpaces + 1 : right])
                res.append(s1 + blank(avgSpaces) + s2)
            return res

        return rearrange(words, maxWidth)
```

## 复杂度分析
* time m
* space m

## 相关题目
1. 待补充
