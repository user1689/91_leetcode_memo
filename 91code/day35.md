## 题目
https://leetcode-cn.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions/

## 思路
hashTable+count

## python
```python3
class Solution:
    def minCharacters(self, a: str, b: str) -> int:

        # 抓特征：分界问题，需要找到划分界限
        # 界限：以26个字母中的某一个为界，其中一个字符串所有字符改成另一个字符串中界限的另一侧
        # bruteForce
        # 统计词频率
        countA = [0 for _ in range(26)]
        countB = [0 for _ in range(26)]
        for char in a:
            countA[ord(char) - ord('a')] += 1
        for char in b:
            countB[ord(char) - ord('a')] += 1
        
        # 暴力枚举borderline
        res = inf
        for borderline in range(0, 26):   

            # corner case
            # 如果borderline为字母a 无法统计小于a的字母数
            if borderline > 0:
                # condition1
                change = 0
                for j in range(borderline, 26):
                    change += countA[j]
                for k in range(0, borderline):
                    change += countB[k]
                res = min(change, res)

                # condition2
                change = 0
                for j in range(0, borderline):
                    change += countA[j]
                for k in range(borderline, 26):
                    change += countB[k]
                res = min(change, res)
            
            # condition3
            change = 0
            for i in range(0, 26):
                if i != borderline:
                    change += countA[i] 
                    change += countB[i]
            res = min(change, res)
            
        return res  
```
## 复杂度分析
* time n**2
* space n 

## 相关题目
1. 待补充

## 附录
![](https://github.com/user1689/leetcode_memo/blob/main/91code/images/LeetCode_1737.jpeg "算法流程图解") "算法流程图解"
