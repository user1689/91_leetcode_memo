## 题目
https://leetcode-cn.com/problems/compare-version-numbers/

## 思路

## python3
```python3
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        brute force
        
        "1.0.0.1"
        "1.0.0"
  
        1-正确思路是通过十进制累加答案 只要每次两个.之间获得的数值不同就比较大小 若有差异即可得出答案提前返回
        2-trikcy的方法是使用zip_longest(arr1, arr2, fillvalue=0)
  
        '''

        tmp1 = version1.split('.')
        tmp2 = version2.split('.')
        i = 0
        j = 0
        n1 = len(tmp1)
        n2 = len(tmp2)
        while (i < n1 and j < n2):
            num1 = int(tmp1[j])
            num2 = int(tmp2[j])
            if (num1 < num2):
                return -1
            elif (num1 > num2):
                return 1
            i += 1
            j += 1
        if (i < n1):
            while (i < n1):
                if (int(tmp1[i]) > 0):
                    return 1
                i += 1
            return 0
        elif (j < n2):
            while (j < n2):
                if (int(tmp2[j]) > 0):
                    return -1
                j += 1
            return 0
        return 0
```

## 复杂度分析
* time O(N)
* space O(1)

## 相关题目
1. 待补充
