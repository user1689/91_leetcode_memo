## 题目
https://leetcode-cn.com/problems/interleaving-string/

## 思路
dfs + memorization, dp

## python3
```python3
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        '''
        一true为true -> or
        一false为false -> and / ^
        设置接受返回值的参数 如果带有条件 可能会存在都不满足条件的层 那么就会导致未定义exception
        '''
         
        def dfs(s1Idx, s2Idx, k):
            if ((s1Idx, s2Idx, k) in dic):
                return dic[(s1Idx, s2Idx, k)]

            if (k == len(s3)):
                dic[(s1Idx, s2Idx, k)] = True
                return dic[(s1Idx, s2Idx, k)]
 
            isValid = False
            
            if (s1Idx < len(s1) and s1[s1Idx] == s3[k]):
                isValid = dfs(s1Idx + 1, s2Idx, k + 1)
            if (s2Idx < len(s2) and s2[s2Idx] == s3[k]):
                isValid = dfs(s1Idx, s2Idx + 1, k + 1) or isValid

            dic[(s1Idx, s2Idx, k)] = isValid
            return dic[(s1Idx, s2Idx, k)]

        if (len(s1) + len(s2) != len(s3)):
            return False
        dic = {}
        return dfs(0, 0, 0)
'''
1.字符串切割
2.传index                
     a                s1 
    / \\      ->     /  \
    a d b           s1   s2
                   ...  /  \
                       s1  s2
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        注意这里s3[i + j - 1]表示的是找s1或s2中是否存在能够
        组成第i + j - 1位的字符, 因为第一位idx=0已被初始化了
        所以当双for从(1,1)开始遍历时候,代表开始寻找idx=1的字
        符了,这样才能符合定义
        '''
        # 状态定义
        # dp[i][j] 表示s1的前i个字符和s2的前j个字符能否构成s3的前i+j个字符
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len + s2_len != len(s3): 
            return False
        dp = [[False for _ in range(s2_len+1)] for _ in range(s1_len+1)]
        dp[0][0] = True
        
        # 初始化
        # 表示 s1 的前 i 位是否能构成 s3 的前 i 位。因此需要满足的条件为，前 i−1 位可以构成 s3 的前 i−1 位且 s1 的第 i 位（s1[i−1]）等于 s3 的第 i 位（s3[i−1]）
        # 从1开始遍历是为了满足状态定义中的 前i位
        for i in range(1, s1_len+1):
            if (dp[i - 1][0] and s1[i - 1] == s3[i - 1]): 
                dp[i][0] = True
            else:
                dp[i][0] = False
        for j in range(1, s2_len+1):
            if (dp[0][j - 1] and s2[j - 1] == s3[j - 1]):
                dp[0][j] = True
            else:
                dp[0][j] = False
                
        # [[True, False, False, False, False, False], 
        # [True, False, False, False, False, False], 
        # [True, False, False, False, False, False], 
        # [False, False, False, False, False, False], 
        # [False, False, False, False, False, False], 
        # [False, False, False, False, False, False]]

        # 开始递推
        for i in range(1, s1_len+1):
            for j in range(1, s2_len+1):
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
        return dp[-1][-1]
```

## 复杂度分析
* time 2**(len(s3))
* space logn

## 相关题目
1. 待补充
        # [True, False, False, False, False, False], 
