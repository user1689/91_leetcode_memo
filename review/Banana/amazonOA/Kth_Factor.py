class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        i = 1
        while (i <= n // i):
            if (n % i == 0):
                k -= 1
                if (k == 0):
                    return i
            i+=1
        
        i-=1    
        if (n // i == i):
            i-=1
        # eg: 
        # n=16 
        # 1, 2, 4, 8, 16
        while (i > 0):
            if (n % i == 0):
                k -= 1
                if (k == 0):
                    return (n // i)
            i-=1
        return -1    


obj = Solution()
n = 16
k = 4
res = obj.kthFactor(n, k)
print(res)