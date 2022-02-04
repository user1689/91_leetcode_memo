## 题目
https://leetcode-cn.com/problems/palindrome-partitioning/

## 思路

## python3
```python3
        '''
        切割字符串
        1 改变s 传递改变后的s
        2 不改变s 传递区间范围
        回文串
        DP预处理
        '''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        切割字符串
        1 改变s 传递改变后的s 
            此时需要注意 字符串被改变以后startIdx就不需要改变了 
        2 不改变s 传递区间范围
            此时字符串没有改变 那么我们需要用startIdx来控制枚举
        '''
        res = []
        path = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(s, startIdx):
            if startIdx == len(s):
                res.append(path[:])
                return
            for i in range(startIdx, len(s)):
                if isPalindrome(s[startIdx : i+1]):
                    path.append(s[startIdx : i+1])
                    backtrack(s, i + 1)
                    path.pop()

        backtrack(s, 0)
        return res

'''
1
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isValid(s, low, high):
            i = low
            j = high
            while (i < j):
                if (s[i] != s[j]):
                    return False
                i += 1
                j -= 1
            return True

        def dfs(startIdx, s):
            if (startIdx == len(s)):
                res.append(path[:])
                return 
            for end in range(startIdx, len(s)):
                if isValid(s, startIdx, end):
                    path.append(s[startIdx:end+1])
                    dfs(end + 1, s)
                    path.pop()
            
        res = []
        path = []
        dfs(0, s)
        return res
             
2
class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        path = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    backtrack(s[i:], path + [s[:i]])

        backtrack(s, path)
        return res
'''
```
## 复杂度分析
* time  n * s^2
* space n^2 

## 相关题目
1. 待补充
