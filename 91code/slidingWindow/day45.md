## 题目
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

## 思路
slidingWindow

## python3
```python3
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # time n
        # space 1
        # 滑动窗口
        res = []
        sCnt = [0 for _ in range(26)]
        pCnt = [0 for _ in range(26)]
        lenP = len(p)
        lenS = len(s)
        if lenS < lenP: return res
        for i in range(lenP):
            pCnt[ord(p[i]) - ord('a')] += 1
            sCnt[ord(s[i]) - ord('a')] += 1
        # print(pCnt)

        if sCnt == pCnt:
            res.append(0)
        for i in range(lenP, lenS):
            sCnt[ord(s[i - lenP]) - ord('a')] -= 1
            sCnt[ord(s[i]) - ord('a')] += 1
            if sCnt == pCnt:
                # right - left + 1 = length
                # left = right - length + 1
                res.append(i - lenP + 1)
        return res
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        # time n
        # space 1
        # 滑动窗口+双指针
        res = []
        lenP = len(p)
        lenS = len(s)
        countP = [0]*26
        countS = [0]*26

        for i in range(lenP):
            countP[ord(p[i]) - ord('a')] += 1
        
        left = 0
        for right in range(0, lenS):
            RightZimu = ord(s[right]) - ord('a')
            countS[RightZimu] += 1
            while countP[RightZimu] < countS[RightZimu]:
                LeftZimu = ord(s[left]) - ord('a')
                countS[LeftZimu] -= 1
                left += 1
            if (right - left + 1) == lenP:
                res.append(left)
        return res


```

## 复杂度分析
* time n
* space 1

## 相关题目
1. https://leetcode-cn.com/problems/permutation-in-string/
