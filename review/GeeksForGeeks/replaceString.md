## 题目
Given an original string input, and two strings S and T, from left to right replace all
occurrences of S in input with T.
Assumptions
• input, S and T are not null, S is not empty string
Examples
• input = "appledogapple", S = "apple", T = "car, input becomes "catdogcat"
• input = "laicode", S = "code", T = "offer", input becomes "laioffer"

## python3
```python3
class solution:
    def changechange(self, input:str, S:str, T:str) -> str:
        P = 131
        MOD = 2**64
        n = len(input)
        p = [1] * (n + 1)
        h = [0] * (n + 1)

        def get(l, r):
            return (h[r] - h[l - 1] * p[r - l + 1]) % MOD
        
        for i in range(0, n):
            p[i+1] = (p[i] * P) % MOD
            h[i+1] = (h[i] * P + ord(input[i])) % MOD
        
        def get2(l, r):
            return (h2[r] - h2[l - 1] * p2[r - l + 1]) % MOD

        m = len(S)
        p2 = [1] * (m + 1)
        h2 = [0] * (m + 1)
        
        for i in range(0, m):
            p2[i+1] = (p2[i] * P) % MOD
            h2[i+1] = (h2[i] * P + ord(S[i])) % MOD
            
        hash_S = get2(1, m)
        error = set()
        for i in range(0, n-m+1):
            print(input[i:i+m])
            hash_cur = get(i+1, i+m)
            if (hash_cur == hash_S):
                error.add(i)
                
        ans = ""
        j = 0
        while(j < n):
            if (j in error):
                tmp = len(S)
                while (tmp > 0):
                    j += 1
                    tmp -= 1
                ans += T
            if (j >= n):
                break
            ans += input[j]
            j += 1
        return ans
                    
        

obj = solution()
# input = "appledogapple"
# S = "apple"
# T = "cat"
input = "laicode"
S = "code"
T = "offer"
obj.changechange(input, S, T)
```
