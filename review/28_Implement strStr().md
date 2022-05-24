## 题目
https://leetcode.cn/problems/implement-strstr/

## 思路
rolling hash

## python3
```python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
    
        '''
        
        算出haystack的p进制前缀数组 记作h
        算出needle的p进制哈希值 记为target
        
        "a"
        ""

        h[0] = 0
        h[1] = h
        h[2] = he
        h[3] = hel
        h[4] = hell
        h[5] = hello
        
            ABCEF
         -  ABC00
               EF
               
           l    r
            12345
            12300 
         -     45
              
        '''
        
        p = [1] * 1010
        h = [0] * 1010
        P = 131
        mod = 2**64
        
        def get(l, r):
            return (h[r] - h[l - 1] * p[r - l + 1]) % mod
        
        n = len(haystack)
        for i in range(0, n):
            p[i+1] = (p[i] * P) % mod
            h[i+1] = (h[i] * P + ord(haystack[i])) % mod
        
        
        m = len(needle)
        target = 0
        for j in range(0, m):
            target = (target * P + ord(needle[j])) % mod
        
        for i in range(0, n - m + 1):
            tmp = get(i+1, i+m)
            if (tmp == target):
                return i
        return -1
        
            
```
## 复杂度分析
time: O(N)  
space: O(N） 

## 相关题目
1. 待补充
